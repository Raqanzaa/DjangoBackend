from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        params = self.request.query_params

        tx_type = params.get("type")
        min_amount = params.get("minAmount")
        max_amount = params.get("maxAmount")

        if tx_type:
            queryset = queryset.filter(type=tx_type)

        if min_amount:
            queryset = queryset.filter(amount__gte=min_amount)

        if max_amount:
            queryset = queryset.filter(amount__lte=max_amount)

        return queryset
    
    def get_serializer_context(self):
        """
        Pass the request context to the serializer.
        This is crucial for the security fix.
        """
        return {'request': self.request}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 🔹 Summary endpoint: total income, expense, balance
    @action(detail=False, methods=['get'])
    def summary(self, request):
        qs = self.get_queryset()
        income = qs.filter(type='IN').aggregate(total=Sum('amount'))['total'] or 0
        expense = qs.filter(type='EX').aggregate(total=Sum('amount'))['total'] or 0
        balance = income - expense
        return Response({
            "income": income,
            "expense": expense,
            "balance": balance
        })

    # 🔹 Grouping by category
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        qs = self.get_queryset()
        data = qs.values('category__id', 'category__name', 'category__type').annotate(
            total=Sum('amount')
        ).order_by('-total')

        return Response(data)
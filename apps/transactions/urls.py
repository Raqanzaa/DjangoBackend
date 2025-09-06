from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TransactionViewSet

# Create a single router instance
router = DefaultRouter()

# Register BOTH ViewSets to this single router
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')

# The router.urls will now contain URLs for both categories and transactions
urlpatterns = router.urls
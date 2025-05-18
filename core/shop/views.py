from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    View
)
from .models import ProductModel, ProductStatusType, ProductCategoryModel
from django.core.exceptions import FieldError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
# from review.models import ReviewModel,ReviewStatusType




class ShopProductGridView(ListView):
    template_name = "shop/product-grid.html"


    queryset = ProductModel.objects.filter(
        status=ProductStatusType.publish.value
    )
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context
        # context["wishlist_items"] = WishlistProductModel.objects.filter(user=self.request.user).values_list(
        #     "product__id", flat=True) if self.request.user.is_authenticated else []
        # context["categories"] = ProductCategoryModel.objects.all()
        # return context


class ShopProductDetailView(DetailView):
    template_name = "shop/product-detail.html"
    queryset = ProductModel.objects.filter(
        status=ProductStatusType.publish.value)


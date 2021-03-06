from django.contrib import admin
from django.utils.html import format_html

from modeltranslation.admin import TranslationAdmin

from klanad.models import (
    Product,
    Company,
    Contact,
    ProductImage,
    ProductGroupImage,
    ProductGroup,
    KlanadTranslations,
    GroupContainer,
)


admin.site.register(Company)
admin.site.register(Contact)


@admin.register(GroupContainer)
class GroupContainerAdmin(TranslationAdmin):
    """Admin for GroupContainers."""

    list_display = ("title", "position")
    list_editable = ("position", )


@admin.register(KlanadTranslations)
class KlanadTranslationAdmin(TranslationAdmin):
    """Admin for the various dynamic fields of the website."""

    def has_add_permission(self, request):
        """Overloaded to prevent more than 1 object being created."""
        if self.model.objects.count() > 1:
            return False
        else:
            super().has_add_permission(request)


class ProductImageInline(admin.TabularInline):
    """Inline ProductImage for the Product admin."""

    model = ProductImage
    readonly_fields = ("preview",)

    def preview(self, obj: ProductImage) -> str:
        """Display a preview of the image."""
        html = '<a href="{url}" target="_blank"><img src="{url}" /></a>'
        return format_html("".join(html.format(url=obj.image.url)))


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    """Product admin page."""

    list_display = ("title", "position", "group", "archived")
    list_editable = ("position", "group", "archived")
    inlines = [ProductImageInline]


class ProductGroupImageInline(admin.TabularInline):
    """Inline ProductImage for the ProductGroup admin."""

    model = ProductGroupImage
    readonly_fields = ("preview",)

    def preview(self, obj: ProductImage) -> str:
        """Display a preview of the image."""
        html = '<a href="{url}" target="_blank"><img src="{url}" /></a>'
        return format_html("".join(html.format(url=obj.image.url)))


@admin.register(ProductGroup)
class ProductGroupAdmin(TranslationAdmin):
    """Product admin page."""

    list_display = ("title", "position", "container", "archived")
    list_editable = ("position", "container", "archived")
    inlines = [ProductGroupImageInline]

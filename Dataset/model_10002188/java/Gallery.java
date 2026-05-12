





import java.util.List;
import java.util.ArrayList;

public class Gallery  {

    private String DateCreate;
    private int ProductID;
    private String Image;
    private int GalleryID;
    private String GalleryName;





    private Products products;


    public Gallery(
        String DateCreate,        int ProductID,        String Image,        int GalleryID,        String GalleryName    ) {
        this.DateCreate = DateCreate;
        this.ProductID = ProductID;
        this.Image = Image;
        this.GalleryID = GalleryID;
        this.GalleryName = GalleryName;
    }


    public String getDatecreate() {
        return DateCreate;
    }

    public void setDatecreate(String DateCreate) {
        this.DateCreate = DateCreate;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public String getImage() {
        return Image;
    }

    public void setImage(String Image) {
        this.Image = Image;
    }
    public int getGalleryid() {
        return GalleryID;
    }

    public void setGalleryid(int GalleryID) {
        this.GalleryID = GalleryID;
    }
    public String getGalleryname() {
        return GalleryName;
    }

    public void setGalleryname(String GalleryName) {
        this.GalleryName = GalleryName;
    }

    public Products getProducts() {
        return products;
    }

    public void setProducts(Products products) {
        this.products = products;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int ProductID;
    private String ProductImage;
    private String ProductType;
    private String ProductDescription;
    private String ProductName;
    private float ProductPrice;



    public Product(
        int ProductID,        String ProductImage,        String ProductType,        String ProductDescription,        String ProductName,        float ProductPrice    ) {
        this.ProductID = ProductID;
        this.ProductImage = ProductImage;
        this.ProductType = ProductType;
        this.ProductDescription = ProductDescription;
        this.ProductName = ProductName;
        this.ProductPrice = ProductPrice;
    }


    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public String getProductimage() {
        return ProductImage;
    }

    public void setProductimage(String ProductImage) {
        this.ProductImage = ProductImage;
    }
    public String getProducttype() {
        return ProductType;
    }

    public void setProducttype(String ProductType) {
        this.ProductType = ProductType;
    }
    public String getProductdescription() {
        return ProductDescription;
    }

    public void setProductdescription(String ProductDescription) {
        this.ProductDescription = ProductDescription;
    }
    public String getProductname() {
        return ProductName;
    }

    public void setProductname(String ProductName) {
        this.ProductName = ProductName;
    }
    public float getProductprice() {
        return ProductPrice;
    }

    public void setProductprice(float ProductPrice) {
        this.ProductPrice = ProductPrice;
    }


}
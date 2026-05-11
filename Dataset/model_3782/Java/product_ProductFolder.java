





import java.util.List;
import java.util.ArrayList;

public class product_ProductFolder extends ProductEntity {






    private product_ProductResourcesContainer product_productresourcescontainer;




    private List<product_ProductFolder> product_productfolders;


    public product_ProductFolder(
    ) {
        super(
        );
        this.product_productfolders = new ArrayList<>();
    }

    public product_ProductFolder(
        ArrayList<product_ProductFolder> product_productfolders    ) {
        this.product_productfolders = product_productfolders;
    }


    public product_ProductResourcesContainer getProduct_productresourcescontainer() {
        return product_productresourcescontainer;
    }

    public void setProduct_productresourcescontainer(product_ProductResourcesContainer product_productresourcescontainer) {
        this.product_productresourcescontainer = product_productresourcescontainer;
    }
    public List<product_ProductFolder> getProduct_productfolders() {
        return product_productfolders;
    }

    public void addProduct_productfolder(Product_productfolder product_productfolder) {
        this.product_productfolders.add(product_productfolder);
    }

}
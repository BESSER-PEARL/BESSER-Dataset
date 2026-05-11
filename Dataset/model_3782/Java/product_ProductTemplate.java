





import java.util.List;
import java.util.ArrayList;

public class product_ProductTemplate extends ProductEntity {

    private String generateToPath;





    private product_ProductFolder product_productfolder;




    private product_ProductComponent product_productcomponent;




    private product_ProductResourcesContainer product_productresourcescontainer;


    public product_ProductTemplate(
        String generateToPath    ) {
        super(
        );
        this.generateToPath = generateToPath;
    }


    public String getGeneratetopath() {
        return generateToPath;
    }

    public void setGeneratetopath(String generateToPath) {
        this.generateToPath = generateToPath;
    }

    public product_ProductFolder getProduct_productfolder() {
        return product_productfolder;
    }

    public void setProduct_productfolder(product_ProductFolder product_productfolder) {
        this.product_productfolder = product_productfolder;
    }
    public product_ProductComponent getProduct_productcomponent() {
        return product_productcomponent;
    }

    public void setProduct_productcomponent(product_ProductComponent product_productcomponent) {
        this.product_productcomponent = product_productcomponent;
    }
    public product_ProductResourcesContainer getProduct_productresourcescontainer() {
        return product_productresourcescontainer;
    }

    public void setProduct_productresourcescontainer(product_ProductResourcesContainer product_productresourcescontainer) {
        this.product_productresourcescontainer = product_productresourcescontainer;
    }

}
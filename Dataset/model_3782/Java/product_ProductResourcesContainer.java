





import java.util.List;
import java.util.ArrayList;

public class product_ProductResourcesContainer  {

    private String name;





    private product_ProductImplementationElements product_productimplementationelements;


    public product_ProductResourcesContainer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public product_ProductImplementationElements getProduct_productimplementationelements() {
        return product_productimplementationelements;
    }

    public void setProduct_productimplementationelements(product_ProductImplementationElements product_productimplementationelements) {
        this.product_productimplementationelements = product_productimplementationelements;
    }

}
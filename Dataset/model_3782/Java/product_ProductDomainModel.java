





import java.util.List;
import java.util.ArrayList;

public class product_ProductDomainModel  {

    private String elements;
    private String name;





    private product_ProductDomainModels product_productdomainmodels;


    public product_ProductDomainModel(
        String elements,        String name    ) {
        this.elements = elements;
        this.name = name;
    }


    public String getElements() {
        return elements;
    }

    public void setElements(String elements) {
        this.elements = elements;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public product_ProductDomainModels getProduct_productdomainmodels() {
        return product_productdomainmodels;
    }

    public void setProduct_productdomainmodels(product_ProductDomainModels product_productdomainmodels) {
        this.product_productdomainmodels = product_productdomainmodels;
    }

}
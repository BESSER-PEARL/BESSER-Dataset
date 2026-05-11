





import java.util.List;
import java.util.ArrayList;

public class sipme_EnterpriseProduct extends EnterpriseObject {

    private String productState;
    private String productNarure;



    public sipme_EnterpriseProduct(
        String productState,        String productNarure    ) {
        super(
        );
        this.productState = productState;
        this.productNarure = productNarure;
    }


    public String getProductstate() {
        return productState;
    }

    public void setProductstate(String productState) {
        this.productState = productState;
    }
    public String getProductnarure() {
        return productNarure;
    }

    public void setProductnarure(String productNarure) {
        this.productNarure = productNarure;
    }


}
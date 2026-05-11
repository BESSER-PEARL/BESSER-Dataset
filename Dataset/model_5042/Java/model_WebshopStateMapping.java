





import java.util.List;
import java.util.ArrayList;

public class model_WebshopStateMapping extends IEntity {

    private String webshopState;
    private String fakturamaOrderState;





    private model_WebShop model_webshop;


    public model_WebshopStateMapping(
        String webshopState,        String fakturamaOrderState    ) {
        super(
        );
        this.webshopState = webshopState;
        this.fakturamaOrderState = fakturamaOrderState;
    }


    public String getWebshopstate() {
        return webshopState;
    }

    public void setWebshopstate(String webshopState) {
        this.webshopState = webshopState;
    }
    public String getFakturamaorderstate() {
        return fakturamaOrderState;
    }

    public void setFakturamaorderstate(String fakturamaOrderState) {
        this.fakturamaOrderState = fakturamaOrderState;
    }

    public model_WebShop getModel_webshop() {
        return model_webshop;
    }

    public void setModel_webshop(model_WebShop model_webshop) {
        this.model_webshop = model_webshop;
    }

}
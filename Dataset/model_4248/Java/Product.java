





import java.util.List;
import java.util.ArrayList;

public class Product  {






    private restapp_model_Price restapp_model_price;




    private restapp_model_ProductsPurchase restapp_model_productspurchase;




    private restapp_model_ProductsCard restapp_model_productscard;


    public Product(
    ) {
    }



    public restapp_model_Price getRestapp_model_price() {
        return restapp_model_price;
    }

    public void setRestapp_model_price(restapp_model_Price restapp_model_price) {
        this.restapp_model_price = restapp_model_price;
    }
    public restapp_model_ProductsPurchase getRestapp_model_productspurchase() {
        return restapp_model_productspurchase;
    }

    public void setRestapp_model_productspurchase(restapp_model_ProductsPurchase restapp_model_productspurchase) {
        this.restapp_model_productspurchase = restapp_model_productspurchase;
    }
    public restapp_model_ProductsCard getRestapp_model_productscard() {
        return restapp_model_productscard;
    }

    public void setRestapp_model_productscard(restapp_model_ProductsCard restapp_model_productscard) {
        this.restapp_model_productscard = restapp_model_productscard;
    }

}
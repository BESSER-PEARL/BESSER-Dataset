





import java.util.List;
import java.util.ArrayList;

public class gives_feedback_UseCase  {






    private shoppingcart_Actor shoppingcart_actor;




    private customer_Actor customer_actor;


    public gives_feedback_UseCase(
    ) {
    }



    public shoppingcart_Actor getShoppingcart_actor() {
        return shoppingcart_actor;
    }

    public void setShoppingcart_actor(shoppingcart_Actor shoppingcart_actor) {
        this.shoppingcart_actor = shoppingcart_actor;
    }
    public customer_Actor getCustomer_actor() {
        return customer_actor;
    }

    public void setCustomer_actor(customer_Actor customer_actor) {
        this.customer_actor = customer_actor;
    }

}
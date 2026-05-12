





import java.util.List;
import java.util.ArrayList;

public class Authentication_Actor  {






    private View_items_UseCase view_items_usecase;




    private Checkout_UseCase checkout_usecase;




    private Client_Register_UseCase client_register_usecase;


    public Authentication_Actor(
    ) {
    }



    public View_items_UseCase getView_items_usecase() {
        return view_items_usecase;
    }

    public void setView_items_usecase(View_items_UseCase view_items_usecase) {
        this.view_items_usecase = view_items_usecase;
    }
    public Checkout_UseCase getCheckout_usecase() {
        return checkout_usecase;
    }

    public void setCheckout_usecase(Checkout_UseCase checkout_usecase) {
        this.checkout_usecase = checkout_usecase;
    }
    public Client_Register_UseCase getClient_register_usecase() {
        return client_register_usecase;
    }

    public void setClient_register_usecase(Client_Register_UseCase client_register_usecase) {
        this.client_register_usecase = client_register_usecase;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Move_items_into_basket_UseCase  {






    private View_Items_UseCase view_items_usecase;




    private Checkout_UseCase checkout_usecase;


    public Move_items_into_basket_UseCase(
    ) {
    }



    public View_Items_UseCase getView_items_usecase() {
        return view_items_usecase;
    }

    public void setView_items_usecase(View_Items_UseCase view_items_usecase) {
        this.view_items_usecase = view_items_usecase;
    }
    public Checkout_UseCase getCheckout_usecase() {
        return checkout_usecase;
    }

    public void setCheckout_usecase(Checkout_UseCase checkout_usecase) {
        this.checkout_usecase = checkout_usecase;
    }

}
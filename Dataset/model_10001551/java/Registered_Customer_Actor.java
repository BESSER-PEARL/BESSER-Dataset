





import java.util.List;
import java.util.ArrayList;

public class Registered_Customer_Actor  {






    private View_items_UseCase view_items_usecase;




    private Make_Purchase_UseCase make_purchase_usecase;


    public Registered_Customer_Actor(
    ) {
    }



    public View_items_UseCase getView_items_usecase() {
        return view_items_usecase;
    }

    public void setView_items_usecase(View_items_UseCase view_items_usecase) {
        this.view_items_usecase = view_items_usecase;
    }
    public Make_Purchase_UseCase getMake_purchase_usecase() {
        return make_purchase_usecase;
    }

    public void setMake_purchase_usecase(Make_Purchase_UseCase make_purchase_usecase) {
        this.make_purchase_usecase = make_purchase_usecase;
    }

}
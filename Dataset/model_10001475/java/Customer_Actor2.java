





import java.util.List;
import java.util.ArrayList;

public class Customer_Actor2  {






    private Add_items_to_shopping_cart_UseCase add_items_to_shopping_cart_usecase;




    private Save_items_for_later_UseCase save_items_for_later_usecase;


    public Customer_Actor2(
    ) {
    }



    public Add_items_to_shopping_cart_UseCase getAdd_items_to_shopping_cart_usecase() {
        return add_items_to_shopping_cart_usecase;
    }

    public void setAdd_items_to_shopping_cart_usecase(Add_items_to_shopping_cart_UseCase add_items_to_shopping_cart_usecase) {
        this.add_items_to_shopping_cart_usecase = add_items_to_shopping_cart_usecase;
    }
    public Save_items_for_later_UseCase getSave_items_for_later_usecase() {
        return save_items_for_later_usecase;
    }

    public void setSave_items_for_later_usecase(Save_items_for_later_UseCase save_items_for_later_usecase) {
        this.save_items_for_later_usecase = save_items_for_later_usecase;
    }

}
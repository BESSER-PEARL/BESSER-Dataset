





import java.util.List;
import java.util.ArrayList;

public class Customer_Actor1  {






    private add_items_to_shopping_cart_UseCase add_items_to_shopping_cart_usecase;




    private save_items_for_later_in_wish_list_UseCase save_items_for_later_in_wish_list_usecase;


    public Customer_Actor1(
    ) {
    }



    public add_items_to_shopping_cart_UseCase getAdd_items_to_shopping_cart_usecase() {
        return add_items_to_shopping_cart_usecase;
    }

    public void setAdd_items_to_shopping_cart_usecase(add_items_to_shopping_cart_UseCase add_items_to_shopping_cart_usecase) {
        this.add_items_to_shopping_cart_usecase = add_items_to_shopping_cart_usecase;
    }
    public save_items_for_later_in_wish_list_UseCase getSave_items_for_later_in_wish_list_usecase() {
        return save_items_for_later_in_wish_list_usecase;
    }

    public void setSave_items_for_later_in_wish_list_usecase(save_items_for_later_in_wish_list_UseCase save_items_for_later_in_wish_list_usecase) {
        this.save_items_for_later_in_wish_list_usecase = save_items_for_later_in_wish_list_usecase;
    }

}
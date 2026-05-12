





import java.util.List;
import java.util.ArrayList;

public class Registered_User_Actor  {






    private Save_favourite_order_UseCase save_favourite_order_usecase;




    private Checkout_UseCase checkout_usecase;




    private View_Pizza_types_UseCase view_pizza_types_usecase;




    private Search_store_locations_UseCase search_store_locations_usecase;




    private Create_Account_UseCase create_account_usecase;




    private Create_your_own_pizza_UseCase create_your_own_pizza_usecase;




    private View_side_orders_UseCase view_side_orders_usecase;




    private Order_tracking_UseCase order_tracking_usecase;


    public Registered_User_Actor(
    ) {
    }



    public Save_favourite_order_UseCase getSave_favourite_order_usecase() {
        return save_favourite_order_usecase;
    }

    public void setSave_favourite_order_usecase(Save_favourite_order_UseCase save_favourite_order_usecase) {
        this.save_favourite_order_usecase = save_favourite_order_usecase;
    }
    public Checkout_UseCase getCheckout_usecase() {
        return checkout_usecase;
    }

    public void setCheckout_usecase(Checkout_UseCase checkout_usecase) {
        this.checkout_usecase = checkout_usecase;
    }
    public View_Pizza_types_UseCase getView_pizza_types_usecase() {
        return view_pizza_types_usecase;
    }

    public void setView_pizza_types_usecase(View_Pizza_types_UseCase view_pizza_types_usecase) {
        this.view_pizza_types_usecase = view_pizza_types_usecase;
    }
    public Search_store_locations_UseCase getSearch_store_locations_usecase() {
        return search_store_locations_usecase;
    }

    public void setSearch_store_locations_usecase(Search_store_locations_UseCase search_store_locations_usecase) {
        this.search_store_locations_usecase = search_store_locations_usecase;
    }
    public Create_Account_UseCase getCreate_account_usecase() {
        return create_account_usecase;
    }

    public void setCreate_account_usecase(Create_Account_UseCase create_account_usecase) {
        this.create_account_usecase = create_account_usecase;
    }
    public Create_your_own_pizza_UseCase getCreate_your_own_pizza_usecase() {
        return create_your_own_pizza_usecase;
    }

    public void setCreate_your_own_pizza_usecase(Create_your_own_pizza_UseCase create_your_own_pizza_usecase) {
        this.create_your_own_pizza_usecase = create_your_own_pizza_usecase;
    }
    public View_side_orders_UseCase getView_side_orders_usecase() {
        return view_side_orders_usecase;
    }

    public void setView_side_orders_usecase(View_side_orders_UseCase view_side_orders_usecase) {
        this.view_side_orders_usecase = view_side_orders_usecase;
    }
    public Order_tracking_UseCase getOrder_tracking_usecase() {
        return order_tracking_usecase;
    }

    public void setOrder_tracking_usecase(Order_tracking_UseCase order_tracking_usecase) {
        this.order_tracking_usecase = order_tracking_usecase;
    }

}
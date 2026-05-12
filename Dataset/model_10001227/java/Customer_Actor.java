





import java.util.List;
import java.util.ArrayList;

public class Customer_Actor  {






    private Log_In_UseCase log_in_usecase;




    private Create_your_own_pizza_UseCase create_your_own_pizza_usecase;




    private Order_tracking_UseCase order_tracking_usecase;




    private View_Pizza_types_UseCase view_pizza_types_usecase;




    private View_side_orders_UseCase view_side_orders_usecase;




    private Visit_home_page_UseCase visit_home_page_usecase;




    private Write_feedback_UseCase write_feedback_usecase;




    private Change_password_UseCase change_password_usecase;




    private Make_payment_UseCase make_payment_usecase;




    private Add_to_cart_and_buy_UseCase add_to_cart_and_buy_usecase;




    private Registration_UseCase registration_usecase;


    public Customer_Actor(
    ) {
    }



    public Log_In_UseCase getLog_in_usecase() {
        return log_in_usecase;
    }

    public void setLog_in_usecase(Log_In_UseCase log_in_usecase) {
        this.log_in_usecase = log_in_usecase;
    }
    public Create_your_own_pizza_UseCase getCreate_your_own_pizza_usecase() {
        return create_your_own_pizza_usecase;
    }

    public void setCreate_your_own_pizza_usecase(Create_your_own_pizza_UseCase create_your_own_pizza_usecase) {
        this.create_your_own_pizza_usecase = create_your_own_pizza_usecase;
    }
    public Order_tracking_UseCase getOrder_tracking_usecase() {
        return order_tracking_usecase;
    }

    public void setOrder_tracking_usecase(Order_tracking_UseCase order_tracking_usecase) {
        this.order_tracking_usecase = order_tracking_usecase;
    }
    public View_Pizza_types_UseCase getView_pizza_types_usecase() {
        return view_pizza_types_usecase;
    }

    public void setView_pizza_types_usecase(View_Pizza_types_UseCase view_pizza_types_usecase) {
        this.view_pizza_types_usecase = view_pizza_types_usecase;
    }
    public View_side_orders_UseCase getView_side_orders_usecase() {
        return view_side_orders_usecase;
    }

    public void setView_side_orders_usecase(View_side_orders_UseCase view_side_orders_usecase) {
        this.view_side_orders_usecase = view_side_orders_usecase;
    }
    public Visit_home_page_UseCase getVisit_home_page_usecase() {
        return visit_home_page_usecase;
    }

    public void setVisit_home_page_usecase(Visit_home_page_UseCase visit_home_page_usecase) {
        this.visit_home_page_usecase = visit_home_page_usecase;
    }
    public Write_feedback_UseCase getWrite_feedback_usecase() {
        return write_feedback_usecase;
    }

    public void setWrite_feedback_usecase(Write_feedback_UseCase write_feedback_usecase) {
        this.write_feedback_usecase = write_feedback_usecase;
    }
    public Change_password_UseCase getChange_password_usecase() {
        return change_password_usecase;
    }

    public void setChange_password_usecase(Change_password_UseCase change_password_usecase) {
        this.change_password_usecase = change_password_usecase;
    }
    public Make_payment_UseCase getMake_payment_usecase() {
        return make_payment_usecase;
    }

    public void setMake_payment_usecase(Make_payment_UseCase make_payment_usecase) {
        this.make_payment_usecase = make_payment_usecase;
    }
    public Add_to_cart_and_buy_UseCase getAdd_to_cart_and_buy_usecase() {
        return add_to_cart_and_buy_usecase;
    }

    public void setAdd_to_cart_and_buy_usecase(Add_to_cart_and_buy_UseCase add_to_cart_and_buy_usecase) {
        this.add_to_cart_and_buy_usecase = add_to_cart_and_buy_usecase;
    }
    public Registration_UseCase getRegistration_usecase() {
        return registration_usecase;
    }

    public void setRegistration_usecase(Registration_UseCase registration_usecase) {
        this.registration_usecase = registration_usecase;
    }

}
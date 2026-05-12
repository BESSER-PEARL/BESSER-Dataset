





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private View_order_transation_UseCase view_order_transation_usecase;




    private Update_status_of_orders_UseCase update_status_of_orders_usecase;


    public Admin_Actor(
    ) {
    }



    public View_order_transation_UseCase getView_order_transation_usecase() {
        return view_order_transation_usecase;
    }

    public void setView_order_transation_usecase(View_order_transation_UseCase view_order_transation_usecase) {
        this.view_order_transation_usecase = view_order_transation_usecase;
    }
    public Update_status_of_orders_UseCase getUpdate_status_of_orders_usecase() {
        return update_status_of_orders_usecase;
    }

    public void setUpdate_status_of_orders_usecase(Update_status_of_orders_UseCase update_status_of_orders_usecase) {
        this.update_status_of_orders_usecase = update_status_of_orders_usecase;
    }

}
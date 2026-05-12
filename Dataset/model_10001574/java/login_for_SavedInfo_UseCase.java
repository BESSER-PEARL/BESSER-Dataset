





import java.util.List;
import java.util.ArrayList;

public class login_for_SavedInfo_UseCase  {






    private Order_Online_UseCase order_online_usecase;


    public login_for_SavedInfo_UseCase(
    ) {
    }



    public Order_Online_UseCase getOrder_online_usecase() {
        return order_online_usecase;
    }

    public void setOrder_online_usecase(Order_Online_UseCase order_online_usecase) {
        this.order_online_usecase = order_online_usecase;
    }

}
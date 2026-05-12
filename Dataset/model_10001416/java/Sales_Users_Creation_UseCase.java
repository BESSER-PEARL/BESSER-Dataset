





import java.util.List;
import java.util.ArrayList;

public class Sales_Users_Creation_UseCase  {






    private Support_User_Actor support_user_actor;




    private Sales_User_Actor sales_user_actor;


    public Sales_Users_Creation_UseCase(
    ) {
    }



    public Support_User_Actor getSupport_user_actor() {
        return support_user_actor;
    }

    public void setSupport_user_actor(Support_User_Actor support_user_actor) {
        this.support_user_actor = support_user_actor;
    }
    public Sales_User_Actor getSales_user_actor() {
        return sales_user_actor;
    }

    public void setSales_user_actor(Sales_User_Actor sales_user_actor) {
        this.sales_user_actor = sales_user_actor;
    }

}
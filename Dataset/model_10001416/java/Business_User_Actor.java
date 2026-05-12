





import java.util.List;
import java.util.ArrayList;

public class Business_User_Actor  {






    private Order_Approved_Rejected_external order_approved_rejected_external;




    private Manage_Sales_Users_external manage_sales_users_external;




    private Notifications_for_Order_Tracking_external notifications_for_order_tracking_external;




    private Assign_Roles_external assign_roles_external;




    private Business_Users_Creation_UseCase business_users_creation_usecase;




    private Manage_Accounts_external manage_accounts_external;




    private Login_and_authentication_external login_and_authentication_external;




    private Login_and_authentication_UseCase login_and_authentication_usecase;


    public Business_User_Actor(
    ) {
    }



    public Order_Approved_Rejected_external getOrder_approved_rejected_external() {
        return order_approved_rejected_external;
    }

    public void setOrder_approved_rejected_external(Order_Approved_Rejected_external order_approved_rejected_external) {
        this.order_approved_rejected_external = order_approved_rejected_external;
    }
    public Manage_Sales_Users_external getManage_sales_users_external() {
        return manage_sales_users_external;
    }

    public void setManage_sales_users_external(Manage_Sales_Users_external manage_sales_users_external) {
        this.manage_sales_users_external = manage_sales_users_external;
    }
    public Notifications_for_Order_Tracking_external getNotifications_for_order_tracking_external() {
        return notifications_for_order_tracking_external;
    }

    public void setNotifications_for_order_tracking_external(Notifications_for_Order_Tracking_external notifications_for_order_tracking_external) {
        this.notifications_for_order_tracking_external = notifications_for_order_tracking_external;
    }
    public Assign_Roles_external getAssign_roles_external() {
        return assign_roles_external;
    }

    public void setAssign_roles_external(Assign_Roles_external assign_roles_external) {
        this.assign_roles_external = assign_roles_external;
    }
    public Business_Users_Creation_UseCase getBusiness_users_creation_usecase() {
        return business_users_creation_usecase;
    }

    public void setBusiness_users_creation_usecase(Business_Users_Creation_UseCase business_users_creation_usecase) {
        this.business_users_creation_usecase = business_users_creation_usecase;
    }
    public Manage_Accounts_external getManage_accounts_external() {
        return manage_accounts_external;
    }

    public void setManage_accounts_external(Manage_Accounts_external manage_accounts_external) {
        this.manage_accounts_external = manage_accounts_external;
    }
    public Login_and_authentication_external getLogin_and_authentication_external() {
        return login_and_authentication_external;
    }

    public void setLogin_and_authentication_external(Login_and_authentication_external login_and_authentication_external) {
        this.login_and_authentication_external = login_and_authentication_external;
    }
    public Login_and_authentication_UseCase getLogin_and_authentication_usecase() {
        return login_and_authentication_usecase;
    }

    public void setLogin_and_authentication_usecase(Login_and_authentication_UseCase login_and_authentication_usecase) {
        this.login_and_authentication_usecase = login_and_authentication_usecase;
    }

}
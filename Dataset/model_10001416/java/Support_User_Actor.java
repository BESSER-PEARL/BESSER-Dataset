





import java.util.List;
import java.util.ArrayList;

public class Support_User_Actor  {






    private Business_Users_Creation_external business_users_creation_external;




    private Login_and_authentication_external login_and_authentication_external;




    private Assign_Roles_external assign_roles_external;




    private Sales_Users_Creation_UseCase1 sales_users_creation_usecase1;




    private Notifications_for_Order_Tracking_external notifications_for_order_tracking_external;




    private Manage_Sales_Users_external manage_sales_users_external;




    private Manage_Accounts_external manage_accounts_external;


    public Support_User_Actor(
    ) {
    }



    public Business_Users_Creation_external getBusiness_users_creation_external() {
        return business_users_creation_external;
    }

    public void setBusiness_users_creation_external(Business_Users_Creation_external business_users_creation_external) {
        this.business_users_creation_external = business_users_creation_external;
    }
    public Login_and_authentication_external getLogin_and_authentication_external() {
        return login_and_authentication_external;
    }

    public void setLogin_and_authentication_external(Login_and_authentication_external login_and_authentication_external) {
        this.login_and_authentication_external = login_and_authentication_external;
    }
    public Assign_Roles_external getAssign_roles_external() {
        return assign_roles_external;
    }

    public void setAssign_roles_external(Assign_Roles_external assign_roles_external) {
        this.assign_roles_external = assign_roles_external;
    }
    public Sales_Users_Creation_UseCase1 getSales_users_creation_usecase1() {
        return sales_users_creation_usecase1;
    }

    public void setSales_users_creation_usecase1(Sales_Users_Creation_UseCase1 sales_users_creation_usecase1) {
        this.sales_users_creation_usecase1 = sales_users_creation_usecase1;
    }
    public Notifications_for_Order_Tracking_external getNotifications_for_order_tracking_external() {
        return notifications_for_order_tracking_external;
    }

    public void setNotifications_for_order_tracking_external(Notifications_for_Order_Tracking_external notifications_for_order_tracking_external) {
        this.notifications_for_order_tracking_external = notifications_for_order_tracking_external;
    }
    public Manage_Sales_Users_external getManage_sales_users_external() {
        return manage_sales_users_external;
    }

    public void setManage_sales_users_external(Manage_Sales_Users_external manage_sales_users_external) {
        this.manage_sales_users_external = manage_sales_users_external;
    }
    public Manage_Accounts_external getManage_accounts_external() {
        return manage_accounts_external;
    }

    public void setManage_accounts_external(Manage_Accounts_external manage_accounts_external) {
        this.manage_accounts_external = manage_accounts_external;
    }

}
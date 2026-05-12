





import java.util.List;
import java.util.ArrayList;

public class Employee_Actor  {






    private Shopping_System_Manage_Order_UseCase shopping_system_manage_order_usecase;




    private Employee_Actor employee_actor;




    private Shopping_System_Login_UseCase shopping_system_login_usecase;




    private Shopping_System_Manage_Bills_UseCase shopping_system_manage_bills_usecase;


    public Employee_Actor(
    ) {
    }



    public Shopping_System_Manage_Order_UseCase getShopping_system_manage_order_usecase() {
        return shopping_system_manage_order_usecase;
    }

    public void setShopping_system_manage_order_usecase(Shopping_System_Manage_Order_UseCase shopping_system_manage_order_usecase) {
        this.shopping_system_manage_order_usecase = shopping_system_manage_order_usecase;
    }
    public Employee_Actor getEmployee_actor() {
        return employee_actor;
    }

    public void setEmployee_actor(Employee_Actor employee_actor) {
        this.employee_actor = employee_actor;
    }
    public Shopping_System_Login_UseCase getShopping_system_login_usecase() {
        return shopping_system_login_usecase;
    }

    public void setShopping_system_login_usecase(Shopping_System_Login_UseCase shopping_system_login_usecase) {
        this.shopping_system_login_usecase = shopping_system_login_usecase;
    }
    public Shopping_System_Manage_Bills_UseCase getShopping_system_manage_bills_usecase() {
        return shopping_system_manage_bills_usecase;
    }

    public void setShopping_system_manage_bills_usecase(Shopping_System_Manage_Bills_UseCase shopping_system_manage_bills_usecase) {
        this.shopping_system_manage_bills_usecase = shopping_system_manage_bills_usecase;
    }

}
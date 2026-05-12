





import java.util.List;
import java.util.ArrayList;

public class Manager_Actor  {






    private Shopping_System_Manage_Catalog_UseCase shopping_system_manage_catalog_usecase;




    private Shopping_System_Login_UseCase shopping_system_login_usecase;




    private Shopping_System_Manage_Settings_UseCase shopping_system_manage_settings_usecase;


    public Manager_Actor(
    ) {
    }



    public Shopping_System_Manage_Catalog_UseCase getShopping_system_manage_catalog_usecase() {
        return shopping_system_manage_catalog_usecase;
    }

    public void setShopping_system_manage_catalog_usecase(Shopping_System_Manage_Catalog_UseCase shopping_system_manage_catalog_usecase) {
        this.shopping_system_manage_catalog_usecase = shopping_system_manage_catalog_usecase;
    }
    public Shopping_System_Login_UseCase getShopping_system_login_usecase() {
        return shopping_system_login_usecase;
    }

    public void setShopping_system_login_usecase(Shopping_System_Login_UseCase shopping_system_login_usecase) {
        this.shopping_system_login_usecase = shopping_system_login_usecase;
    }
    public Shopping_System_Manage_Settings_UseCase getShopping_system_manage_settings_usecase() {
        return shopping_system_manage_settings_usecase;
    }

    public void setShopping_system_manage_settings_usecase(Shopping_System_Manage_Settings_UseCase shopping_system_manage_settings_usecase) {
        this.shopping_system_manage_settings_usecase = shopping_system_manage_settings_usecase;
    }

}
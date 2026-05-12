





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Edit_menu_UseCase edit_menu_usecase;




    private Manage_accounts_UseCase manage_accounts_usecase;


    public Admin_Actor(
    ) {
    }



    public Edit_menu_UseCase getEdit_menu_usecase() {
        return edit_menu_usecase;
    }

    public void setEdit_menu_usecase(Edit_menu_UseCase edit_menu_usecase) {
        this.edit_menu_usecase = edit_menu_usecase;
    }
    public Manage_accounts_UseCase getManage_accounts_usecase() {
        return manage_accounts_usecase;
    }

    public void setManage_accounts_usecase(Manage_accounts_UseCase manage_accounts_usecase) {
        this.manage_accounts_usecase = manage_accounts_usecase;
    }

}
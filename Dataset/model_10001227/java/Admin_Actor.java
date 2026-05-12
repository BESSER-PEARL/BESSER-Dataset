





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Manage_accounts_UseCase manage_accounts_usecase;




    private Edit____delete___view_menu_UseCase edit____delete___view_menu_usecase;


    public Admin_Actor(
    ) {
    }



    public Manage_accounts_UseCase getManage_accounts_usecase() {
        return manage_accounts_usecase;
    }

    public void setManage_accounts_usecase(Manage_accounts_UseCase manage_accounts_usecase) {
        this.manage_accounts_usecase = manage_accounts_usecase;
    }
    public Edit____delete___view_menu_UseCase getEdit____delete___view_menu_usecase() {
        return edit____delete___view_menu_usecase;
    }

    public void setEdit____delete___view_menu_usecase(Edit____delete___view_menu_UseCase edit____delete___view_menu_usecase) {
        this.edit____delete___view_menu_usecase = edit____delete___view_menu_usecase;
    }

}
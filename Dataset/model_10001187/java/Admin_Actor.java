





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Key_generate_UseCase key_generate_usecase;




    private Login_UseCase login_usecase;




    private View_product_UseCase view_product_usecase;




    private Update_product_UseCase update_product_usecase;


    public Admin_Actor(
    ) {
    }



    public Key_generate_UseCase getKey_generate_usecase() {
        return key_generate_usecase;
    }

    public void setKey_generate_usecase(Key_generate_UseCase key_generate_usecase) {
        this.key_generate_usecase = key_generate_usecase;
    }
    public Login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(Login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }
    public View_product_UseCase getView_product_usecase() {
        return view_product_usecase;
    }

    public void setView_product_usecase(View_product_UseCase view_product_usecase) {
        this.view_product_usecase = view_product_usecase;
    }
    public Update_product_UseCase getUpdate_product_usecase() {
        return update_product_usecase;
    }

    public void setUpdate_product_usecase(Update_product_UseCase update_product_usecase) {
        this.update_product_usecase = update_product_usecase;
    }

}
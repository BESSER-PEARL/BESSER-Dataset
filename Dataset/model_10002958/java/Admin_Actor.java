





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Update_product_UseCase update_product_usecase;




    private View_product_UseCase view_product_usecase;




    private Key_generate_UseCase key_generate_usecase;


    public Admin_Actor(
    ) {
    }



    public Update_product_UseCase getUpdate_product_usecase() {
        return update_product_usecase;
    }

    public void setUpdate_product_usecase(Update_product_UseCase update_product_usecase) {
        this.update_product_usecase = update_product_usecase;
    }
    public View_product_UseCase getView_product_usecase() {
        return view_product_usecase;
    }

    public void setView_product_usecase(View_product_UseCase view_product_usecase) {
        this.view_product_usecase = view_product_usecase;
    }
    public Key_generate_UseCase getKey_generate_usecase() {
        return key_generate_usecase;
    }

    public void setKey_generate_usecase(Key_generate_UseCase key_generate_usecase) {
        this.key_generate_usecase = key_generate_usecase;
    }

}






import java.util.List;
import java.util.ArrayList;

public class User_Actor  {






    private Buy_product_UseCase buy_product_usecase;




    private View_product_UseCase view_product_usecase;




    private Key_generate_UseCase key_generate_usecase;


    public User_Actor(
    ) {
    }



    public Buy_product_UseCase getBuy_product_usecase() {
        return buy_product_usecase;
    }

    public void setBuy_product_usecase(Buy_product_UseCase buy_product_usecase) {
        this.buy_product_usecase = buy_product_usecase;
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
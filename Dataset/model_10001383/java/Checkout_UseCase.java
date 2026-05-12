





import java.util.List;
import java.util.ArrayList;

public class Checkout_UseCase  {






    private Choose_items_UseCase choose_items_usecase;




    private make_a_purchase_UseCase make_a_purchase_usecase;


    public Checkout_UseCase(
    ) {
    }



    public Choose_items_UseCase getChoose_items_usecase() {
        return choose_items_usecase;
    }

    public void setChoose_items_usecase(Choose_items_UseCase choose_items_usecase) {
        this.choose_items_usecase = choose_items_usecase;
    }
    public make_a_purchase_UseCase getMake_a_purchase_usecase() {
        return make_a_purchase_usecase;
    }

    public void setMake_a_purchase_usecase(make_a_purchase_UseCase make_a_purchase_usecase) {
        this.make_a_purchase_usecase = make_a_purchase_usecase;
    }

}
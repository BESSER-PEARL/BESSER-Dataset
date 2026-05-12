





import java.util.List;
import java.util.ArrayList;

public class Choose_items_UseCase  {






    private view_items_UseCase view_items_usecase;




    private special_offers_UseCase special_offers_usecase;




    private make_a_purchase_UseCase make_a_purchase_usecase;


    public Choose_items_UseCase(
    ) {
    }



    public view_items_UseCase getView_items_usecase() {
        return view_items_usecase;
    }

    public void setView_items_usecase(view_items_UseCase view_items_usecase) {
        this.view_items_usecase = view_items_usecase;
    }
    public special_offers_UseCase getSpecial_offers_usecase() {
        return special_offers_usecase;
    }

    public void setSpecial_offers_usecase(special_offers_UseCase special_offers_usecase) {
        this.special_offers_usecase = special_offers_usecase;
    }
    public make_a_purchase_UseCase getMake_a_purchase_usecase() {
        return make_a_purchase_usecase;
    }

    public void setMake_a_purchase_usecase(make_a_purchase_UseCase make_a_purchase_usecase) {
        this.make_a_purchase_usecase = make_a_purchase_usecase;
    }

}
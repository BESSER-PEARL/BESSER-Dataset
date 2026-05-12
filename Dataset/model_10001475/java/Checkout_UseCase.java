





import java.util.List;
import java.util.ArrayList;

public class Checkout_UseCase  {






    private Points_and_Special_Offers_UseCase points_and_special_offers_usecase;


    public Checkout_UseCase(
    ) {
    }



    public Points_and_Special_Offers_UseCase getPoints_and_special_offers_usecase() {
        return points_and_special_offers_usecase;
    }

    public void setPoints_and_special_offers_usecase(Points_and_Special_Offers_UseCase points_and_special_offers_usecase) {
        this.points_and_special_offers_usecase = points_and_special_offers_usecase;
    }

}
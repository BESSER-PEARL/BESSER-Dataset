





import java.util.List;
import java.util.ArrayList;

public class Distribute_UseCase  {






    private OnlineBuy_UseCase onlinebuy_usecase;




    private Seller_Actor seller_actor;


    public Distribute_UseCase(
    ) {
    }



    public OnlineBuy_UseCase getOnlinebuy_usecase() {
        return onlinebuy_usecase;
    }

    public void setOnlinebuy_usecase(OnlineBuy_UseCase onlinebuy_usecase) {
        this.onlinebuy_usecase = onlinebuy_usecase;
    }
    public Seller_Actor getSeller_actor() {
        return seller_actor;
    }

    public void setSeller_actor(Seller_Actor seller_actor) {
        this.seller_actor = seller_actor;
    }

}
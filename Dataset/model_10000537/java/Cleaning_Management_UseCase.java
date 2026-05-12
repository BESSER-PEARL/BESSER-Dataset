





import java.util.List;
import java.util.ArrayList;

public class Cleaning_Management_UseCase  {






    private Info_UseCase info_usecase;




    private Delivery_Management_UseCase delivery_management_usecase;




    private Cleaner_Actor cleaner_actor;


    public Cleaning_Management_UseCase(
    ) {
    }



    public Info_UseCase getInfo_usecase() {
        return info_usecase;
    }

    public void setInfo_usecase(Info_UseCase info_usecase) {
        this.info_usecase = info_usecase;
    }
    public Delivery_Management_UseCase getDelivery_management_usecase() {
        return delivery_management_usecase;
    }

    public void setDelivery_management_usecase(Delivery_Management_UseCase delivery_management_usecase) {
        this.delivery_management_usecase = delivery_management_usecase;
    }
    public Cleaner_Actor getCleaner_actor() {
        return cleaner_actor;
    }

    public void setCleaner_actor(Cleaner_Actor cleaner_actor) {
        this.cleaner_actor = cleaner_actor;
    }

}
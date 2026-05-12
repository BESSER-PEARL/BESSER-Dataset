





import java.util.List;
import java.util.ArrayList;

public class Deliver_Actor  {






    private Delivery_Management_UseCase delivery_management_usecase;




    private Delivery_Boy_Id_UseCase delivery_boy_id_usecase;


    public Deliver_Actor(
    ) {
    }



    public Delivery_Management_UseCase getDelivery_management_usecase() {
        return delivery_management_usecase;
    }

    public void setDelivery_management_usecase(Delivery_Management_UseCase delivery_management_usecase) {
        this.delivery_management_usecase = delivery_management_usecase;
    }
    public Delivery_Boy_Id_UseCase getDelivery_boy_id_usecase() {
        return delivery_boy_id_usecase;
    }

    public void setDelivery_boy_id_usecase(Delivery_Boy_Id_UseCase delivery_boy_id_usecase) {
        this.delivery_boy_id_usecase = delivery_boy_id_usecase;
    }

}
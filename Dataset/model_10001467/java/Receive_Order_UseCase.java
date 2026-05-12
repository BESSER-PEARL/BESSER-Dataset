





import java.util.List;
import java.util.ArrayList;

public class Receive_Order_UseCase  {






    private Admin_Actor admin_actor;




    private Delivery_Person_Actor delivery_person_actor;


    public Receive_Order_UseCase(
    ) {
    }



    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }
    public Delivery_Person_Actor getDelivery_person_actor() {
        return delivery_person_actor;
    }

    public void setDelivery_person_actor(Delivery_Person_Actor delivery_person_actor) {
        this.delivery_person_actor = delivery_person_actor;
    }

}
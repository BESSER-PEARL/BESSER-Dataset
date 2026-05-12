





import java.util.List;
import java.util.ArrayList;

public class Register__UseCase  {






    private Delivery_Person_Actor delivery_person_actor;




    private Admin_Actor admin_actor;


    public Register__UseCase(
    ) {
    }



    public Delivery_Person_Actor getDelivery_person_actor() {
        return delivery_person_actor;
    }

    public void setDelivery_person_actor(Delivery_Person_Actor delivery_person_actor) {
        this.delivery_person_actor = delivery_person_actor;
    }
    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }

}
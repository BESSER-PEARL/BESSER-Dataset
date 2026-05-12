





import java.util.List;
import java.util.ArrayList;

public class Receive_order_UseCase  {






    private Pizza_Chef_Actor pizza_chef_actor;




    private Delivery_person_Actor delivery_person_actor;


    public Receive_order_UseCase(
    ) {
    }



    public Pizza_Chef_Actor getPizza_chef_actor() {
        return pizza_chef_actor;
    }

    public void setPizza_chef_actor(Pizza_Chef_Actor pizza_chef_actor) {
        this.pizza_chef_actor = pizza_chef_actor;
    }
    public Delivery_person_Actor getDelivery_person_actor() {
        return delivery_person_actor;
    }

    public void setDelivery_person_actor(Delivery_person_Actor delivery_person_actor) {
        this.delivery_person_actor = delivery_person_actor;
    }

}
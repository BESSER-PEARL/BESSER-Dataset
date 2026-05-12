





import java.util.List;
import java.util.ArrayList;

public class USECASE1_Goal  {






    private List<Service> services;




    private List<Actor> actors;


    public USECASE1_Goal(
    ) {
        this.services = new ArrayList<>();
        this.actors = new ArrayList<>();
    }

    public USECASE1_Goal(
        ArrayList<Service> services,        ArrayList<Actor> actors    ) {
        this.services = services;
        this.actors = actors;
    }


    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }
    public List<Actor> getActors() {
        return actors;
    }

    public void addActor(Actor actor) {
        this.actors.add(actor);
    }

}
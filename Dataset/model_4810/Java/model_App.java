





import java.util.List;
import java.util.ArrayList;

public class model_App  {






    private List<model_Service> model_services;




    private List<model_User> model_users;


    public model_App(
    ) {
        this.model_services = new ArrayList<>();
        this.model_users = new ArrayList<>();
    }

    public model_App(
        ArrayList<model_Service> model_services,        ArrayList<model_User> model_users    ) {
        this.model_services = model_services;
        this.model_users = model_users;
    }


    public List<model_Service> getModel_services() {
        return model_services;
    }

    public void addModel_service(Model_service model_service) {
        this.model_services.add(model_service);
    }
    public List<model_User> getModel_users() {
        return model_users;
    }

    public void addModel_user(Model_user model_user) {
        this.model_users.add(model_user);
    }

}
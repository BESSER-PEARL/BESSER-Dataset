





import java.util.List;
import java.util.ArrayList;

public class model_WikiProject extends Internal {






    private List<model_User> model_users;


    public model_WikiProject(
    ) {
        super(
        );
        this.model_users = new ArrayList<>();
    }

    public model_WikiProject(
        ArrayList<model_User> model_users    ) {
        this.model_users = model_users;
    }


    public List<model_User> getModel_users() {
        return model_users;
    }

    public void addModel_user(Model_user model_user) {
        this.model_users.add(model_user);
    }

}
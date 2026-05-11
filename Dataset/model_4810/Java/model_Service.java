





import java.util.List;
import java.util.ArrayList;

public class model_Service  {

    private String name;
    private String acceptedParams;
    private String methodName;





    private List<model_User> model_users;


    public model_Service(
        String name,        String acceptedParams,        String methodName    ) {
        this.name = name;
        this.acceptedParams = acceptedParams;
        this.methodName = methodName;
        this.model_users = new ArrayList<>();
    }

    public model_Service(
        String name,        String acceptedParams,        String methodName        ArrayList<model_User> model_users    ) {
        this.name = name;
        this.acceptedParams = acceptedParams;
        this.methodName = methodName;
        this.model_users = model_users;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAcceptedparams() {
        return acceptedParams;
    }

    public void setAcceptedparams(String acceptedParams) {
        this.acceptedParams = acceptedParams;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }

    public List<model_User> getModel_users() {
        return model_users;
    }

    public void addModel_user(Model_user model_user) {
        this.model_users.add(model_user);
    }

}
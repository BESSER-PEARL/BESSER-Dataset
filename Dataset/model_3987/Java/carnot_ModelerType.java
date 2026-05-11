





import java.util.List;
import java.util.ArrayList;

public class carnot_ModelerType extends IIdentifiableModelElement {

    private String password;
    private String email;





    private carnot_ModelType carnot_modeltype;


    public carnot_ModelerType(
        String password,        String email    ) {
        super(
        );
        this.password = password;
        this.email = email;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}
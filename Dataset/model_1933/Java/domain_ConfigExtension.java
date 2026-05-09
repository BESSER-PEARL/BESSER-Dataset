





import java.util.List;
import java.util.ArrayList;

public class domain_ConfigExtension  {

    private String uid;





    private domain_Configuration domain_configuration;




    private domain_Recipes domain_recipes;




    private domain_Configuration domain_configuration;


    public domain_ConfigExtension(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Configuration getDomain_configuration() {
        return domain_configuration;
    }

    public void setDomain_configuration(domain_Configuration domain_configuration) {
        this.domain_configuration = domain_configuration;
    }
    public domain_Recipes getDomain_recipes() {
        return domain_recipes;
    }

    public void setDomain_recipes(domain_Recipes domain_recipes) {
        this.domain_recipes = domain_recipes;
    }
    public domain_Configuration getDomain_configuration() {
        return domain_configuration;
    }

    public void setDomain_configuration(domain_Configuration domain_configuration) {
        this.domain_configuration = domain_configuration;
    }

}
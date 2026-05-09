





import java.util.List;
import java.util.ArrayList;

public class domain_Configuration  {

    private String uid;
    private String name;





    private domain_Recipes domain_recipes;


    public domain_Configuration(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domain_Recipes getDomain_recipes() {
        return domain_recipes;
    }

    public void setDomain_recipes(domain_Recipes domain_recipes) {
        this.domain_recipes = domain_recipes;
    }

}
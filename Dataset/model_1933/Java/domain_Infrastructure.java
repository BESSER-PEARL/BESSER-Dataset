





import java.util.List;
import java.util.ArrayList;

public class domain_Infrastructure  {

    private String name;
    private String uid;





    private domain_Configuration domain_configuration;




    private domain_Recipes domain_recipes;




    private domain_Recipe domain_recipe;




    private domain_Configuration domain_configuration;




    private domain_Recipe domain_recipe;


    public domain_Infrastructure(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public domain_Recipe getDomain_recipe() {
        return domain_recipe;
    }

    public void setDomain_recipe(domain_Recipe domain_recipe) {
        this.domain_recipe = domain_recipe;
    }
    public domain_Configuration getDomain_configuration() {
        return domain_configuration;
    }

    public void setDomain_configuration(domain_Configuration domain_configuration) {
        this.domain_configuration = domain_configuration;
    }
    public domain_Recipe getDomain_recipe() {
        return domain_recipe;
    }

    public void setDomain_recipe(domain_Recipe domain_recipe) {
        this.domain_recipe = domain_recipe;
    }

}
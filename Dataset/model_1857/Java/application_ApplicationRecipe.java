





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationRecipe  {

    private String uid;
    private String name;





    private application_ApplicationRecipes application_applicationrecipes;


    public application_ApplicationRecipe(
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

    public application_ApplicationRecipes getApplication_applicationrecipes() {
        return application_applicationrecipes;
    }

    public void setApplication_applicationrecipes(application_ApplicationRecipes application_applicationrecipes) {
        this.application_applicationrecipes = application_applicationrecipes;
    }

}
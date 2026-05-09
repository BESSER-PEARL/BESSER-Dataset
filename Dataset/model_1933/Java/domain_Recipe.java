





import java.util.List;
import java.util.ArrayList;

public class domain_Recipe extends UsingMappers {

    private String name;
    private String uid;





    private domain_Recipes domain_recipes;




    private domain_Recipes domain_recipes;




    private domain_Ingredient domain_ingredient;




    private List<domain_Ingredient> domain_ingredients;


    public domain_Recipe(
        String name,        String uid    ) {
        super(
        );
        this.name = name;
        this.uid = uid;
        this.domain_ingredients = new ArrayList<>();
    }

    public domain_Recipe(
        String name,        String uid        ArrayList<domain_Ingredient> domain_ingredients    ) {
        this.name = name;
        this.uid = uid;
        this.domain_ingredients = domain_ingredients;
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

    public domain_Recipes getDomain_recipes() {
        return domain_recipes;
    }

    public void setDomain_recipes(domain_Recipes domain_recipes) {
        this.domain_recipes = domain_recipes;
    }
    public domain_Recipes getDomain_recipes() {
        return domain_recipes;
    }

    public void setDomain_recipes(domain_Recipes domain_recipes) {
        this.domain_recipes = domain_recipes;
    }
    public domain_Ingredient getDomain_ingredient() {
        return domain_ingredient;
    }

    public void setDomain_ingredient(domain_Ingredient domain_ingredient) {
        this.domain_ingredient = domain_ingredient;
    }
    public List<domain_Ingredient> getDomain_ingredients() {
        return domain_ingredients;
    }

    public void addDomain_ingredient(Domain_ingredient domain_ingredient) {
        this.domain_ingredients.add(domain_ingredient);
    }

}
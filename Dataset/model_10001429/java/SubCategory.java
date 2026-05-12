





import java.util.List;
import java.util.ArrayList;

public class SubCategory  {

    private int id;
    private int cat_id;
    private String name;





    private List<Category> categorys;




    private Category category;




    private SubCategory subcategory;


    public SubCategory(
        int id,        int cat_id,        String name    ) {
        this.id = id;
        this.cat_id = cat_id;
        this.name = name;
        this.categorys = new ArrayList<>();
    }

    public SubCategory(
        int id,        int cat_id,        String name        ArrayList<Category> categorys    ) {
        this.id = id;
        this.cat_id = cat_id;
        this.name = name;
        this.categorys = categorys;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getCat_id() {
        return cat_id;
    }

    public void setCat_id(int cat_id) {
        this.cat_id = cat_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Category> getCategorys() {
        return categorys;
    }

    public void addCategory(Category category) {
        this.categorys.add(category);
    }
    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }
    public SubCategory getSubcategory() {
        return subcategory;
    }

    public void setSubcategory(SubCategory subcategory) {
        this.subcategory = subcategory;
    }

}
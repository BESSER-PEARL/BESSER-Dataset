





import java.util.List;
import java.util.ArrayList;

public class newP_Specification  {

    private String name;





    private List<newP_Category> newp_categorys;


    public newP_Specification(
        String name    ) {
        this.name = name;
        this.newp_categorys = new ArrayList<>();
    }

    public newP_Specification(
        String name        ArrayList<newP_Category> newp_categorys    ) {
        this.name = name;
        this.newp_categorys = newp_categorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<newP_Category> getNewp_categorys() {
        return newp_categorys;
    }

    public void addNewp_category(Newp_category newp_category) {
        this.newp_categorys.add(newp_category);
    }

}
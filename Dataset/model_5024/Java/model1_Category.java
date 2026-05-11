





import java.util.List;
import java.util.ArrayList;

public class model1_Category  {

    private String name;





    private List<model1_Category> model1_categorys;




    private model1_Company model1_company;


    public model1_Category(
        String name    ) {
        this.name = name;
        this.model1_categorys = new ArrayList<>();
    }

    public model1_Category(
        String name        ArrayList<model1_Category> model1_categorys    ) {
        this.name = name;
        this.model1_categorys = model1_categorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model1_Category> getModel1_categorys() {
        return model1_categorys;
    }

    public void addModel1_category(Model1_category model1_category) {
        this.model1_categorys.add(model1_category);
    }
    public model1_Company getModel1_company() {
        return model1_company;
    }

    public void setModel1_company(model1_Company model1_company) {
        this.model1_company = model1_company;
    }

}






import java.util.List;
import java.util.ArrayList;

public class model1_Category  {

    private String name;





    private model1_Company model1_company;




    private model1_Category model1_category;


    public model1_Category(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model1_Company getModel1_company() {
        return model1_company;
    }

    public void setModel1_company(model1_Company model1_company) {
        this.model1_company = model1_company;
    }
    public model1_Category getModel1_category() {
        return model1_category;
    }

    public void setModel1_category(model1_Category model1_category) {
        this.model1_category = model1_category;
    }

}
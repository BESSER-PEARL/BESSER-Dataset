





import java.util.List;
import java.util.ArrayList;

public class model_ModelPropertyCategory  {

    private String description;
    private String name;





    private List<model_ModelPropertyCategory> model_modelpropertycategorys;




    private model_ModelPropertyCategory model_modelpropertycategory;


    public model_ModelPropertyCategory(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.model_modelpropertycategorys = new ArrayList<>();
    }

    public model_ModelPropertyCategory(
        String description,        String name        ArrayList<model_ModelPropertyCategory> model_modelpropertycategorys    ) {
        this.description = description;
        this.name = name;
        this.model_modelpropertycategorys = model_modelpropertycategorys;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model_ModelPropertyCategory> getModel_modelpropertycategorys() {
        return model_modelpropertycategorys;
    }

    public void addModel_modelpropertycategory(Model_modelpropertycategory model_modelpropertycategory) {
        this.model_modelpropertycategorys.add(model_modelpropertycategory);
    }
    public model_ModelPropertyCategory getModel_modelpropertycategory() {
        return model_modelpropertycategory;
    }

    public void setModel_modelpropertycategory(model_ModelPropertyCategory model_modelpropertycategory) {
        this.model_modelpropertycategory = model_modelpropertycategory;
    }

}






import java.util.List;
import java.util.ArrayList;

public class model_ModelPropertyType  {

    private String defaultValue;
    private String name;
    private String description;
    private String admissibleValues;
    private String id;





    private model_ModelPropertyCategory model_modelpropertycategory;




    private model_ModelPropertyCategory model_modelpropertycategory;


    public model_ModelPropertyType(
        String defaultValue,        String name,        String description,        String admissibleValues,        String id    ) {
        this.defaultValue = defaultValue;
        this.name = name;
        this.description = description;
        this.admissibleValues = admissibleValues;
        this.id = id;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAdmissiblevalues() {
        return admissibleValues;
    }

    public void setAdmissiblevalues(String admissibleValues) {
        this.admissibleValues = admissibleValues;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public model_ModelPropertyCategory getModel_modelpropertycategory() {
        return model_modelpropertycategory;
    }

    public void setModel_modelpropertycategory(model_ModelPropertyCategory model_modelpropertycategory) {
        this.model_modelpropertycategory = model_modelpropertycategory;
    }
    public model_ModelPropertyCategory getModel_modelpropertycategory() {
        return model_modelpropertycategory;
    }

    public void setModel_modelpropertycategory(model_ModelPropertyCategory model_modelpropertycategory) {
        this.model_modelpropertycategory = model_modelpropertycategory;
    }

}
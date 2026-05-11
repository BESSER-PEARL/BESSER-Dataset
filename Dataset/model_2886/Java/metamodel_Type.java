





import java.util.List;
import java.util.ArrayList;

public class metamodel_Type  {

    private String name;





    private metamodel_Model metamodel_model;




    private metamodel_parameter metamodel_parameter;


    public metamodel_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_Model getMetamodel_model() {
        return metamodel_model;
    }

    public void setMetamodel_model(metamodel_Model metamodel_model) {
        this.metamodel_model = metamodel_model;
    }
    public metamodel_parameter getMetamodel_parameter() {
        return metamodel_parameter;
    }

    public void setMetamodel_parameter(metamodel_parameter metamodel_parameter) {
        this.metamodel_parameter = metamodel_parameter;
    }

}
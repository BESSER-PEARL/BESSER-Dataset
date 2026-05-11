





import java.util.List;
import java.util.ArrayList;

public class metamodel_Type  {

    private String name;





    private metamodel_Feature metamodel_feature;




    private metamodel_Model metamodel_model;


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

    public metamodel_Feature getMetamodel_feature() {
        return metamodel_feature;
    }

    public void setMetamodel_feature(metamodel_Feature metamodel_feature) {
        this.metamodel_feature = metamodel_feature;
    }
    public metamodel_Model getMetamodel_model() {
        return metamodel_model;
    }

    public void setMetamodel_model(metamodel_Model metamodel_model) {
        this.metamodel_model = metamodel_model;
    }

}
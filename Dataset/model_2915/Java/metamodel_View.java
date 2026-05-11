





import java.util.List;
import java.util.ArrayList;

public class metamodel_View extends Type {






    private metamodel_Controller metamodel_controller;




    private metamodel_Model metamodel_model;


    public metamodel_View(
    ) {
        super(
        );
    }



    public metamodel_Controller getMetamodel_controller() {
        return metamodel_controller;
    }

    public void setMetamodel_controller(metamodel_Controller metamodel_controller) {
        this.metamodel_controller = metamodel_controller;
    }
    public metamodel_Model getMetamodel_model() {
        return metamodel_model;
    }

    public void setMetamodel_model(metamodel_Model metamodel_model) {
        this.metamodel_model = metamodel_model;
    }

}
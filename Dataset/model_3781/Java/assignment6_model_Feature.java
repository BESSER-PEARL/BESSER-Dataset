





import java.util.List;
import java.util.ArrayList;

public class assignment6_model_Feature  {

    private boolean mandatory;
    private boolean selected;
    private String name;





    private assignment6_model_Configurator assignment6_model_configurator;




    private assignment6_model_Feature assignment6_model_feature;


    public assignment6_model_Feature(
        boolean mandatory,        boolean selected,        String name    ) {
        this.mandatory = mandatory;
        this.selected = selected;
        this.name = name;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public assignment6_model_Configurator getAssignment6_model_configurator() {
        return assignment6_model_configurator;
    }

    public void setAssignment6_model_configurator(assignment6_model_Configurator assignment6_model_configurator) {
        this.assignment6_model_configurator = assignment6_model_configurator;
    }
    public assignment6_model_Feature getAssignment6_model_feature() {
        return assignment6_model_feature;
    }

    public void setAssignment6_model_feature(assignment6_model_Feature assignment6_model_feature) {
        this.assignment6_model_feature = assignment6_model_feature;
    }

}






import java.util.List;
import java.util.ArrayList;

public class assignment6_model_Group  {

    private String name;
    private String groupType;





    private assignment6_model_Feature assignment6_model_feature;




    private assignment6_model_Configurator assignment6_model_configurator;


    public assignment6_model_Group(
        String name,        String groupType    ) {
        this.name = name;
        this.groupType = groupType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGrouptype() {
        return groupType;
    }

    public void setGrouptype(String groupType) {
        this.groupType = groupType;
    }

    public assignment6_model_Feature getAssignment6_model_feature() {
        return assignment6_model_feature;
    }

    public void setAssignment6_model_feature(assignment6_model_Feature assignment6_model_feature) {
        this.assignment6_model_feature = assignment6_model_feature;
    }
    public assignment6_model_Configurator getAssignment6_model_configurator() {
        return assignment6_model_configurator;
    }

    public void setAssignment6_model_configurator(assignment6_model_Configurator assignment6_model_configurator) {
        this.assignment6_model_configurator = assignment6_model_configurator;
    }

}
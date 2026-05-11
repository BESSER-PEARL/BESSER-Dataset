





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Reaction  {






    private iotdsl_Rule iotdsl_rule;




    private iotdsl_Actuating iotdsl_actuating;




    private iotdsl_NodeInstance iotdsl_nodeinstance;




    private List<iotdsl_Attribute> iotdsl_attributes;


    public iotdsl_Reaction(
    ) {
        this.iotdsl_attributes = new ArrayList<>();
    }

    public iotdsl_Reaction(
        ArrayList<iotdsl_Attribute> iotdsl_attributes    ) {
        this.iotdsl_attributes = iotdsl_attributes;
    }


    public iotdsl_Rule getIotdsl_rule() {
        return iotdsl_rule;
    }

    public void setIotdsl_rule(iotdsl_Rule iotdsl_rule) {
        this.iotdsl_rule = iotdsl_rule;
    }
    public iotdsl_Actuating getIotdsl_actuating() {
        return iotdsl_actuating;
    }

    public void setIotdsl_actuating(iotdsl_Actuating iotdsl_actuating) {
        this.iotdsl_actuating = iotdsl_actuating;
    }
    public iotdsl_NodeInstance getIotdsl_nodeinstance() {
        return iotdsl_nodeinstance;
    }

    public void setIotdsl_nodeinstance(iotdsl_NodeInstance iotdsl_nodeinstance) {
        this.iotdsl_nodeinstance = iotdsl_nodeinstance;
    }
    public List<iotdsl_Attribute> getIotdsl_attributes() {
        return iotdsl_attributes;
    }

    public void addIotdsl_attribute(Iotdsl_attribute iotdsl_attribute) {
        this.iotdsl_attributes.add(iotdsl_attribute);
    }

}
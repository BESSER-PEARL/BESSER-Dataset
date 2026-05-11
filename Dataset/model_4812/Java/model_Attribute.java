





import java.util.List;
import java.util.ArrayList;

public class model_Attribute  {

    private int minOccurs;
    private int maxOccurs;





    private model_BasicRelationship model_basicrelationship;




    private model_BasicObject model_basicobject;




    private model_BasicObject model_basicobject;


    public model_Attribute(
        int minOccurs,        int maxOccurs    ) {
        this.minOccurs = minOccurs;
        this.maxOccurs = maxOccurs;
    }


    public int getMinoccurs() {
        return minOccurs;
    }

    public void setMinoccurs(int minOccurs) {
        this.minOccurs = minOccurs;
    }
    public int getMaxoccurs() {
        return maxOccurs;
    }

    public void setMaxoccurs(int maxOccurs) {
        this.maxOccurs = maxOccurs;
    }

    public model_BasicRelationship getModel_basicrelationship() {
        return model_basicrelationship;
    }

    public void setModel_basicrelationship(model_BasicRelationship model_basicrelationship) {
        this.model_basicrelationship = model_basicrelationship;
    }
    public model_BasicObject getModel_basicobject() {
        return model_basicobject;
    }

    public void setModel_basicobject(model_BasicObject model_basicobject) {
        this.model_basicobject = model_basicobject;
    }
    public model_BasicObject getModel_basicobject() {
        return model_basicobject;
    }

    public void setModel_basicobject(model_BasicObject model_basicobject) {
        this.model_basicobject = model_basicobject;
    }

}
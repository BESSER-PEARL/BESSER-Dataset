





import java.util.List;
import java.util.ArrayList;

public class diva_Property extends NamedElement {

    private String direction;





    private diva_VariabilityModel diva_variabilitymodel;




    private diva_Priority diva_priority;




    private diva_PropertyValue diva_propertyvalue;




    private diva_PropertyPriority diva_propertypriority;




    private diva_Score diva_score;


    public diva_Property(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public diva_VariabilityModel getDiva_variabilitymodel() {
        return diva_variabilitymodel;
    }

    public void setDiva_variabilitymodel(diva_VariabilityModel diva_variabilitymodel) {
        this.diva_variabilitymodel = diva_variabilitymodel;
    }
    public diva_Priority getDiva_priority() {
        return diva_priority;
    }

    public void setDiva_priority(diva_Priority diva_priority) {
        this.diva_priority = diva_priority;
    }
    public diva_PropertyValue getDiva_propertyvalue() {
        return diva_propertyvalue;
    }

    public void setDiva_propertyvalue(diva_PropertyValue diva_propertyvalue) {
        this.diva_propertyvalue = diva_propertyvalue;
    }
    public diva_PropertyPriority getDiva_propertypriority() {
        return diva_propertypriority;
    }

    public void setDiva_propertypriority(diva_PropertyPriority diva_propertypriority) {
        this.diva_propertypriority = diva_propertypriority;
    }
    public diva_Score getDiva_score() {
        return diva_score;
    }

    public void setDiva_score(diva_Score diva_score) {
        this.diva_score = diva_score;
    }

}
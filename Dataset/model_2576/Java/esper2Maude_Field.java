





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_Field  {

    private String eventPropName;
    private String star;
    private String eventVariable;



    public esper2Maude_Field(
        String eventPropName,        String star,        String eventVariable    ) {
        this.eventPropName = eventPropName;
        this.star = star;
        this.eventVariable = eventVariable;
    }


    public String getEventpropname() {
        return eventPropName;
    }

    public void setEventpropname(String eventPropName) {
        this.eventPropName = eventPropName;
    }
    public String getStar() {
        return star;
    }

    public void setStar(String star) {
        this.star = star;
    }
    public String getEventvariable() {
        return eventVariable;
    }

    public void setEventvariable(String eventVariable) {
        this.eventVariable = eventVariable;
    }


}
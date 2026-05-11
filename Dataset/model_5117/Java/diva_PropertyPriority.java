





import java.util.List;
import java.util.ArrayList;

public class diva_PropertyPriority extends DiVAModelElement {

    private String priority;





    private diva_Property diva_property;


    public diva_PropertyPriority(
        String priority    ) {
        super(
        );
        this.priority = priority;
    }


    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public diva_Property getDiva_property() {
        return diva_property;
    }

    public void setDiva_property(diva_Property diva_property) {
        this.diva_property = diva_property;
    }

}
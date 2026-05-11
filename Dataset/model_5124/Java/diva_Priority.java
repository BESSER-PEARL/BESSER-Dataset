





import java.util.List;
import java.util.ArrayList;

public class diva_Priority extends DiVAModelElement {

    private int priority;





    private diva_Property diva_property;




    private diva_Context diva_context;


    public diva_Priority(
        int priority    ) {
        super(
        );
        this.priority = priority;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public diva_Property getDiva_property() {
        return diva_property;
    }

    public void setDiva_property(diva_Property diva_property) {
        this.diva_property = diva_property;
    }
    public diva_Context getDiva_context() {
        return diva_context;
    }

    public void setDiva_context(diva_Context diva_context) {
        this.diva_context = diva_context;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ric_MessageDialogButton  {

    private String label;
    private String event;





    private ric_MessageDialog ric_messagedialog;


    public ric_MessageDialogButton(
        String label,        String event    ) {
        this.label = label;
        this.event = event;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public ric_MessageDialog getRic_messagedialog() {
        return ric_messagedialog;
    }

    public void setRic_messagedialog(ric_MessageDialog ric_messagedialog) {
        this.ric_messagedialog = ric_messagedialog;
    }

}
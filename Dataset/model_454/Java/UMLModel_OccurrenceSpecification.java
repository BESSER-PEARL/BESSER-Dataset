





import java.util.List;
import java.util.ArrayList;

public class UMLModel_OccurrenceSpecification extends InteractionFragment {

    private String toBefore;
    private String event;
    private String toAfter;



    public UMLModel_OccurrenceSpecification(
        String toBefore,        String event,        String toAfter    ) {
        super(
        );
        this.toBefore = toBefore;
        this.event = event;
        this.toAfter = toAfter;
    }


    public String getTobefore() {
        return toBefore;
    }

    public void setTobefore(String toBefore) {
        this.toBefore = toBefore;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getToafter() {
        return toAfter;
    }

    public void setToafter(String toAfter) {
        this.toAfter = toAfter;
    }


}
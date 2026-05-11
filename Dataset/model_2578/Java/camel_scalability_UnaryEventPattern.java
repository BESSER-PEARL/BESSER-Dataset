





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_UnaryEventPattern extends EventPattern {

    private String operator;
    private int occurrenceNum;





    private Event event;


    public camel_scalability_UnaryEventPattern(
        String operator,        int occurrenceNum    ) {
        super(
        );
        this.operator = operator;
        this.occurrenceNum = occurrenceNum;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public int getOccurrencenum() {
        return occurrenceNum;
    }

    public void setOccurrencenum(int occurrenceNum) {
        this.occurrenceNum = occurrenceNum;
    }

    public Event getEvent() {
        return event;
    }

    public void setEvent(Event event) {
        this.event = event;
    }

}
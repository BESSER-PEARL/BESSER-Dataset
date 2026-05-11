





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_BinaryEventPattern extends EventPattern {

    private int lowerOccurrenceBound;
    private int upperOccurrenceBound;
    private String operator;





    private Event event;




    private Event event;


    public camel_scalability_BinaryEventPattern(
        int lowerOccurrenceBound,        int upperOccurrenceBound,        String operator    ) {
        super(
        );
        this.lowerOccurrenceBound = lowerOccurrenceBound;
        this.upperOccurrenceBound = upperOccurrenceBound;
        this.operator = operator;
    }


    public int getLoweroccurrencebound() {
        return lowerOccurrenceBound;
    }

    public void setLoweroccurrencebound(int lowerOccurrenceBound) {
        this.lowerOccurrenceBound = lowerOccurrenceBound;
    }
    public int getUpperoccurrencebound() {
        return upperOccurrenceBound;
    }

    public void setUpperoccurrencebound(int upperOccurrenceBound) {
        this.upperOccurrenceBound = upperOccurrenceBound;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public Event getEvent() {
        return event;
    }

    public void setEvent(Event event) {
        this.event = event;
    }
    public Event getEvent() {
        return event;
    }

    public void setEvent(Event event) {
        this.event = event;
    }

}






import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_MultipleChoice extends ExamItem {

    private String selectionWay;
    private boolean optional;
    private int numberOfChoices;



    public AssistantMVC_MultipleChoice(
        String selectionWay,        boolean optional,        int numberOfChoices    ) {
        super(
        );
        this.selectionWay = selectionWay;
        this.optional = optional;
        this.numberOfChoices = numberOfChoices;
    }


    public String getSelectionway() {
        return selectionWay;
    }

    public void setSelectionway(String selectionWay) {
        this.selectionWay = selectionWay;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public int getNumberofchoices() {
        return numberOfChoices;
    }

    public void setNumberofchoices(int numberOfChoices) {
        this.numberOfChoices = numberOfChoices;
    }


}
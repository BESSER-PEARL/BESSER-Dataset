





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_MultipleChoiceController extends ExamItemController {

    private int numberOfChoices;
    private String selectionWay;



    public AssistantMVC_MultipleChoiceController(
        int numberOfChoices,        String selectionWay    ) {
        super(
        );
        this.numberOfChoices = numberOfChoices;
        this.selectionWay = selectionWay;
    }


    public int getNumberofchoices() {
        return numberOfChoices;
    }

    public void setNumberofchoices(int numberOfChoices) {
        this.numberOfChoices = numberOfChoices;
    }
    public String getSelectionway() {
        return selectionWay;
    }

    public void setSelectionway(String selectionWay) {
        this.selectionWay = selectionWay;
    }


}
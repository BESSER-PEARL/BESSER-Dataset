





import java.util.List;
import java.util.ArrayList;

public class ryz_MultipleChoice extends PresentationFormElement {

    private boolean multipleSelection;
    private String multipleChoiceType;



    public ryz_MultipleChoice(
        boolean multipleSelection,        String multipleChoiceType    ) {
        super(
        );
        this.multipleSelection = multipleSelection;
        this.multipleChoiceType = multipleChoiceType;
    }


    public boolean getMultipleselection() {
        return multipleSelection;
    }

    public void setMultipleselection(boolean multipleSelection) {
        this.multipleSelection = multipleSelection;
    }
    public String getMultiplechoicetype() {
        return multipleChoiceType;
    }

    public void setMultiplechoicetype(String multipleChoiceType) {
        this.multipleChoiceType = multipleChoiceType;
    }


}
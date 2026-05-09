





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_MultipleChoice extends Multiple, ExamItem {

    private boolean optional;



    public AssistantMVC_MultipleChoice(
        boolean optional    ) {
        super(
        );
        this.optional = optional;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }


}
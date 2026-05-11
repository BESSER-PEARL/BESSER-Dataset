





import java.util.List;
import java.util.ArrayList;

public class forms_CompositionCondition extends Condition {

    private boolean isAnd;





    private List<forms_CompositionCondition> forms_compositionconditions;


    public forms_CompositionCondition(
        boolean isAnd    ) {
        super(
        );
        this.isAnd = isAnd;
        this.forms_compositionconditions = new ArrayList<>();
    }

    public forms_CompositionCondition(
        boolean isAnd        ArrayList<forms_CompositionCondition> forms_compositionconditions    ) {
        this.isAnd = isAnd;
        this.forms_compositionconditions = forms_compositionconditions;
    }

    public boolean getIsand() {
        return isAnd;
    }

    public void setIsand(boolean isAnd) {
        this.isAnd = isAnd;
    }

    public List<forms_CompositionCondition> getForms_compositionconditions() {
        return forms_compositionconditions;
    }

    public void addForms_compositioncondition(Forms_compositioncondition forms_compositioncondition) {
        this.forms_compositionconditions.add(forms_compositioncondition);
    }

}
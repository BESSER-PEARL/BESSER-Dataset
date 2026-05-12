





import java.util.List;
import java.util.ArrayList;

public class pivot_Constraint extends NamedElement {

    private String isCallable;





    private pivot_Transition pivot_transition;




    private pivot_State pivot_state;




    private pivot_Class pivot_class;




    private List<pivot_Element> pivot_elements;




    private pivot_Namespace pivot_namespace;




    private pivot_Operation pivot_operation;




    private pivot_LanguageExpression pivot_languageexpression;




    private pivot_Operation pivot_operation;




    private pivot_Constraint pivot_constraint;




    private pivot_LanguageExpression pivot_languageexpression;




    private pivot_Operation pivot_operation;




    private pivot_Operation pivot_operation;




    private pivot_State pivot_state;




    private pivot_Namespace pivot_namespace;




    private pivot_Transition pivot_transition;


    public pivot_Constraint(
        String isCallable    ) {
        super(
        );
        this.isCallable = isCallable;
        this.pivot_elements = new ArrayList<>();
    }

    public pivot_Constraint(
        String isCallable        ArrayList<pivot_Element> pivot_elements    ) {
        this.isCallable = isCallable;
        this.pivot_elements = pivot_elements;
    }

    public String getIscallable() {
        return isCallable;
    }

    public void setIscallable(String isCallable) {
        this.isCallable = isCallable;
    }

    public pivot_Transition getPivot_transition() {
        return pivot_transition;
    }

    public void setPivot_transition(pivot_Transition pivot_transition) {
        this.pivot_transition = pivot_transition;
    }
    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }
    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }
    public List<pivot_Element> getPivot_elements() {
        return pivot_elements;
    }

    public void addPivot_element(Pivot_element pivot_element) {
        this.pivot_elements.add(pivot_element);
    }
    public pivot_Namespace getPivot_namespace() {
        return pivot_namespace;
    }

    public void setPivot_namespace(pivot_Namespace pivot_namespace) {
        this.pivot_namespace = pivot_namespace;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_LanguageExpression getPivot_languageexpression() {
        return pivot_languageexpression;
    }

    public void setPivot_languageexpression(pivot_LanguageExpression pivot_languageexpression) {
        this.pivot_languageexpression = pivot_languageexpression;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_LanguageExpression getPivot_languageexpression() {
        return pivot_languageexpression;
    }

    public void setPivot_languageexpression(pivot_LanguageExpression pivot_languageexpression) {
        this.pivot_languageexpression = pivot_languageexpression;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }
    public pivot_Namespace getPivot_namespace() {
        return pivot_namespace;
    }

    public void setPivot_namespace(pivot_Namespace pivot_namespace) {
        this.pivot_namespace = pivot_namespace;
    }
    public pivot_Transition getPivot_transition() {
        return pivot_transition;
    }

    public void setPivot_transition(pivot_Transition pivot_transition) {
        this.pivot_transition = pivot_transition;
    }

}
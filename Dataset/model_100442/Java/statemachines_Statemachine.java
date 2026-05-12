





import java.util.List;
import java.util.ArrayList;

public class statemachines_Statemachine extends AbstractExtension, Diagram, EventBNamedCommentedElement {

    private String selfName;
    private String translation;





    private statemachines_Statemachine statemachines_statemachine;


    public statemachines_Statemachine(
        String selfName,        String translation    ) {
        super(
        );
        this.selfName = selfName;
        this.translation = translation;
    }


    public String getSelfname() {
        return selfName;
    }

    public void setSelfname(String selfName) {
        this.selfName = selfName;
    }
    public String getTranslation() {
        return translation;
    }

    public void setTranslation(String translation) {
        this.translation = translation;
    }

    public statemachines_Statemachine getStatemachines_statemachine() {
        return statemachines_statemachine;
    }

    public void setStatemachines_statemachine(statemachines_Statemachine statemachines_statemachine) {
        this.statemachines_statemachine = statemachines_statemachine;
    }

}
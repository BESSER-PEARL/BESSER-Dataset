





import java.util.List;
import java.util.ArrayList;

public class model_Branch  {






    private model_Action model_action;




    private model_IfStatement model_ifstatement;




    private model_SwitchStatement model_switchstatement;




    private model_ChoiceStatement model_choicestatement;


    public model_Branch(
    ) {
    }



    public model_Action getModel_action() {
        return model_action;
    }

    public void setModel_action(model_Action model_action) {
        this.model_action = model_action;
    }
    public model_IfStatement getModel_ifstatement() {
        return model_ifstatement;
    }

    public void setModel_ifstatement(model_IfStatement model_ifstatement) {
        this.model_ifstatement = model_ifstatement;
    }
    public model_SwitchStatement getModel_switchstatement() {
        return model_switchstatement;
    }

    public void setModel_switchstatement(model_SwitchStatement model_switchstatement) {
        this.model_switchstatement = model_switchstatement;
    }
    public model_ChoiceStatement getModel_choicestatement() {
        return model_choicestatement;
    }

    public void setModel_choicestatement(model_ChoiceStatement model_choicestatement) {
        this.model_choicestatement = model_choicestatement;
    }

}
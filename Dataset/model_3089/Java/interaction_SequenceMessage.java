





import java.util.List;
import java.util.ArrayList;

public class interaction_SequenceMessage extends NamedElement {

    private String kind;





    private interaction_Part interaction_part;




    private interaction_AbstractFunction interaction_abstractfunction;




    private interaction_Part interaction_part;




    private interaction_AbstractFunction interaction_abstractfunction;




    private List<interaction_SequenceMessageValuation> interaction_sequencemessagevaluations;




    private interaction_Scenario interaction_scenario;


    public interaction_SequenceMessage(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.interaction_sequencemessagevaluations = new ArrayList<>();
    }

    public interaction_SequenceMessage(
        String kind        ArrayList<interaction_SequenceMessageValuation> interaction_sequencemessagevaluations    ) {
        this.kind = kind;
        this.interaction_sequencemessagevaluations = interaction_sequencemessagevaluations;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public interaction_Part getInteraction_part() {
        return interaction_part;
    }

    public void setInteraction_part(interaction_Part interaction_part) {
        this.interaction_part = interaction_part;
    }
    public interaction_AbstractFunction getInteraction_abstractfunction() {
        return interaction_abstractfunction;
    }

    public void setInteraction_abstractfunction(interaction_AbstractFunction interaction_abstractfunction) {
        this.interaction_abstractfunction = interaction_abstractfunction;
    }
    public interaction_Part getInteraction_part() {
        return interaction_part;
    }

    public void setInteraction_part(interaction_Part interaction_part) {
        this.interaction_part = interaction_part;
    }
    public interaction_AbstractFunction getInteraction_abstractfunction() {
        return interaction_abstractfunction;
    }

    public void setInteraction_abstractfunction(interaction_AbstractFunction interaction_abstractfunction) {
        this.interaction_abstractfunction = interaction_abstractfunction;
    }
    public List<interaction_SequenceMessageValuation> getInteraction_sequencemessagevaluations() {
        return interaction_sequencemessagevaluations;
    }

    public void addInteraction_sequencemessagevaluation(Interaction_sequencemessagevaluation interaction_sequencemessagevaluation) {
        this.interaction_sequencemessagevaluations.add(interaction_sequencemessagevaluation);
    }
    public interaction_Scenario getInteraction_scenario() {
        return interaction_scenario;
    }

    public void setInteraction_scenario(interaction_Scenario interaction_scenario) {
        this.interaction_scenario = interaction_scenario;
    }

}






import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMOperator  {

    private String kind;





    private List<SAMOperator> samoperators;




    private List<SAMSchemaValue> samschemavalues;




    private List<SAMOperator> samoperators;




    private List<SAMSchemaAction> samschemaactions;


    public behavioral_status_and_action_old_SAMOperator(
        String kind    ) {
        this.kind = kind;
        this.samoperators = new ArrayList<>();
        this.samschemavalues = new ArrayList<>();
        this.samoperators = new ArrayList<>();
        this.samschemaactions = new ArrayList<>();
    }

    public behavioral_status_and_action_old_SAMOperator(
        String kind        ArrayList<SAMOperator> samoperators,        ArrayList<SAMSchemaValue> samschemavalues,        ArrayList<SAMOperator> samoperators,        ArrayList<SAMSchemaAction> samschemaactions    ) {
        this.kind = kind;
        this.samoperators = samoperators;
        this.samschemavalues = samschemavalues;
        this.samoperators = samoperators;
        this.samschemaactions = samschemaactions;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<SAMOperator> getSamoperators() {
        return samoperators;
    }

    public void addSamoperator(Samoperator samoperator) {
        this.samoperators.add(samoperator);
    }
    public List<SAMSchemaValue> getSamschemavalues() {
        return samschemavalues;
    }

    public void addSamschemavalue(Samschemavalue samschemavalue) {
        this.samschemavalues.add(samschemavalue);
    }
    public List<SAMOperator> getSamoperators() {
        return samoperators;
    }

    public void addSamoperator(Samoperator samoperator) {
        this.samoperators.add(samoperator);
    }
    public List<SAMSchemaAction> getSamschemaactions() {
        return samschemaactions;
    }

    public void addSamschemaaction(Samschemaaction samschemaaction) {
        this.samschemaactions.add(samschemaaction);
    }

}
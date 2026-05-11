





import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMSchemaValue  {

    private boolean isInitial;
    private boolean isInhibiting;





    private List<SAMSchemaValue> samschemavalues;




    private List<SAMSchemaAction> samschemaactions;




    private List<SAMOperator> samoperators;




    private List<SAMSchemaValue> samschemavalues;




    private SAMSchemaVariable samschemavariable;




    private List<SAMSchemaAction> samschemaactions;


    public behavioral_status_and_action_old_SAMSchemaValue(
        boolean isInitial,        boolean isInhibiting    ) {
        this.isInitial = isInitial;
        this.isInhibiting = isInhibiting;
        this.samschemavalues = new ArrayList<>();
        this.samschemaactions = new ArrayList<>();
        this.samoperators = new ArrayList<>();
        this.samschemavalues = new ArrayList<>();
        this.samschemaactions = new ArrayList<>();
    }

    public behavioral_status_and_action_old_SAMSchemaValue(
        boolean isInitial,        boolean isInhibiting        ArrayList<SAMSchemaValue> samschemavalues,        ArrayList<SAMSchemaAction> samschemaactions,        ArrayList<SAMOperator> samoperators,        ArrayList<SAMSchemaValue> samschemavalues,        ArrayList<SAMSchemaAction> samschemaactions    ) {
        this.isInitial = isInitial;
        this.isInhibiting = isInhibiting;
        this.samschemavalues = samschemavalues;
        this.samschemaactions = samschemaactions;
        this.samoperators = samoperators;
        this.samschemavalues = samschemavalues;
        this.samschemaactions = samschemaactions;
    }

    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public boolean getIsinhibiting() {
        return isInhibiting;
    }

    public void setIsinhibiting(boolean isInhibiting) {
        this.isInhibiting = isInhibiting;
    }

    public List<SAMSchemaValue> getSamschemavalues() {
        return samschemavalues;
    }

    public void addSamschemavalue(Samschemavalue samschemavalue) {
        this.samschemavalues.add(samschemavalue);
    }
    public List<SAMSchemaAction> getSamschemaactions() {
        return samschemaactions;
    }

    public void addSamschemaaction(Samschemaaction samschemaaction) {
        this.samschemaactions.add(samschemaaction);
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
    public SAMSchemaVariable getSamschemavariable() {
        return samschemavariable;
    }

    public void setSamschemavariable(SAMSchemaVariable samschemavariable) {
        this.samschemavariable = samschemavariable;
    }
    public List<SAMSchemaAction> getSamschemaactions() {
        return samschemaactions;
    }

    public void addSamschemaaction(Samschemaaction samschemaaction) {
        this.samschemaactions.add(samschemaaction);
    }

}
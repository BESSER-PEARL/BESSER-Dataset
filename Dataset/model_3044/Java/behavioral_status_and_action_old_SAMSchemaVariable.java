





import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMSchemaVariable  {

    private boolean hasStateGuard;





    private List<SAMSchemaValue> samschemavalues;




    private List<SAMSchemaDerivator> samschemaderivators;




    private List<SAMSchemaDerivator> samschemaderivators;




    private SAMStatusVariable samstatusvariable;


    public behavioral_status_and_action_old_SAMSchemaVariable(
        boolean hasStateGuard    ) {
        this.hasStateGuard = hasStateGuard;
        this.samschemavalues = new ArrayList<>();
        this.samschemaderivators = new ArrayList<>();
        this.samschemaderivators = new ArrayList<>();
    }

    public behavioral_status_and_action_old_SAMSchemaVariable(
        boolean hasStateGuard        ArrayList<SAMSchemaValue> samschemavalues,        ArrayList<SAMSchemaDerivator> samschemaderivators,        ArrayList<SAMSchemaDerivator> samschemaderivators    ) {
        this.hasStateGuard = hasStateGuard;
        this.samschemavalues = samschemavalues;
        this.samschemaderivators = samschemaderivators;
        this.samschemaderivators = samschemaderivators;
    }

    public boolean getHasstateguard() {
        return hasStateGuard;
    }

    public void setHasstateguard(boolean hasStateGuard) {
        this.hasStateGuard = hasStateGuard;
    }

    public List<SAMSchemaValue> getSamschemavalues() {
        return samschemavalues;
    }

    public void addSamschemavalue(Samschemavalue samschemavalue) {
        this.samschemavalues.add(samschemavalue);
    }
    public List<SAMSchemaDerivator> getSamschemaderivators() {
        return samschemaderivators;
    }

    public void addSamschemaderivator(Samschemaderivator samschemaderivator) {
        this.samschemaderivators.add(samschemaderivator);
    }
    public List<SAMSchemaDerivator> getSamschemaderivators() {
        return samschemaderivators;
    }

    public void addSamschemaderivator(Samschemaderivator samschemaderivator) {
        this.samschemaderivators.add(samschemaderivator);
    }
    public SAMStatusVariable getSamstatusvariable() {
        return samstatusvariable;
    }

    public void setSamstatusvariable(SAMStatusVariable samstatusvariable) {
        this.samstatusvariable = samstatusvariable;
    }

}
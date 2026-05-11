





import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMSchemaAction  {






    private List<SAMOperator> samoperators;




    private SAMStatusSchema samstatusschema;




    private List<SAMSchemaValue> samschemavalues;




    private List<SAMSchemaValue> samschemavalues;


    public behavioral_status_and_action_old_SAMSchemaAction(
    ) {
        this.samoperators = new ArrayList<>();
        this.samschemavalues = new ArrayList<>();
        this.samschemavalues = new ArrayList<>();
    }

    public behavioral_status_and_action_old_SAMSchemaAction(
        ArrayList<SAMOperator> samoperators,        ArrayList<SAMSchemaValue> samschemavalues,        ArrayList<SAMSchemaValue> samschemavalues    ) {
        this.samoperators = samoperators;
        this.samschemavalues = samschemavalues;
        this.samschemavalues = samschemavalues;
    }


    public List<SAMOperator> getSamoperators() {
        return samoperators;
    }

    public void addSamoperator(Samoperator samoperator) {
        this.samoperators.add(samoperator);
    }
    public SAMStatusSchema getSamstatusschema() {
        return samstatusschema;
    }

    public void setSamstatusschema(SAMStatusSchema samstatusschema) {
        this.samstatusschema = samstatusschema;
    }
    public List<SAMSchemaValue> getSamschemavalues() {
        return samschemavalues;
    }

    public void addSamschemavalue(Samschemavalue samschemavalue) {
        this.samschemavalues.add(samschemavalue);
    }
    public List<SAMSchemaValue> getSamschemavalues() {
        return samschemavalues;
    }

    public void addSamschemavalue(Samschemavalue samschemavalue) {
        this.samschemavalues.add(samschemavalue);
    }

}
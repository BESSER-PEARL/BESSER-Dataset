





import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMStatusSchema  {

    private String name;





    private List<SAMSchemaAction> samschemaactions;




    private List<SAMSchemaVariable> samschemavariables;




    private List<SAMSchemaDerivator> samschemaderivators;




    private SapClass sapclass;


    public behavioral_status_and_action_old_SAMStatusSchema(
        String name    ) {
        this.name = name;
        this.samschemaactions = new ArrayList<>();
        this.samschemavariables = new ArrayList<>();
        this.samschemaderivators = new ArrayList<>();
    }

    public behavioral_status_and_action_old_SAMStatusSchema(
        String name        ArrayList<SAMSchemaAction> samschemaactions,        ArrayList<SAMSchemaVariable> samschemavariables,        ArrayList<SAMSchemaDerivator> samschemaderivators    ) {
        this.name = name;
        this.samschemaactions = samschemaactions;
        this.samschemavariables = samschemavariables;
        this.samschemaderivators = samschemaderivators;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SAMSchemaAction> getSamschemaactions() {
        return samschemaactions;
    }

    public void addSamschemaaction(Samschemaaction samschemaaction) {
        this.samschemaactions.add(samschemaaction);
    }
    public List<SAMSchemaVariable> getSamschemavariables() {
        return samschemavariables;
    }

    public void addSamschemavariable(Samschemavariable samschemavariable) {
        this.samschemavariables.add(samschemavariable);
    }
    public List<SAMSchemaDerivator> getSamschemaderivators() {
        return samschemaderivators;
    }

    public void addSamschemaderivator(Samschemaderivator samschemaderivator) {
        this.samschemaderivators.add(samschemaderivator);
    }
    public SapClass getSapclass() {
        return sapclass;
    }

    public void setSapclass(SapClass sapclass) {
        this.sapclass = sapclass;
    }

}
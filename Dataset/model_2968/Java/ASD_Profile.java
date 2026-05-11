





import java.util.List;
import java.util.ArrayList;

public class ASD_Profile extends NamedElement {






    private ASD_ServiceDescription asd_servicedescription;




    private List<ASD_AssertionSet> asd_assertionsets;




    private ASD_AssertionSet asd_assertionset;




    private ASD_ServiceDescription asd_servicedescription;




    private List<ASD_Operation> asd_operations;


    public ASD_Profile(
    ) {
        super(
        );
        this.asd_assertionsets = new ArrayList<>();
        this.asd_operations = new ArrayList<>();
    }

    public ASD_Profile(
        ArrayList<ASD_AssertionSet> asd_assertionsets,        ArrayList<ASD_Operation> asd_operations    ) {
        this.asd_assertionsets = asd_assertionsets;
        this.asd_operations = asd_operations;
    }


    public ASD_ServiceDescription getAsd_servicedescription() {
        return asd_servicedescription;
    }

    public void setAsd_servicedescription(ASD_ServiceDescription asd_servicedescription) {
        this.asd_servicedescription = asd_servicedescription;
    }
    public List<ASD_AssertionSet> getAsd_assertionsets() {
        return asd_assertionsets;
    }

    public void addAsd_assertionset(Asd_assertionset asd_assertionset) {
        this.asd_assertionsets.add(asd_assertionset);
    }
    public ASD_AssertionSet getAsd_assertionset() {
        return asd_assertionset;
    }

    public void setAsd_assertionset(ASD_AssertionSet asd_assertionset) {
        this.asd_assertionset = asd_assertionset;
    }
    public ASD_ServiceDescription getAsd_servicedescription() {
        return asd_servicedescription;
    }

    public void setAsd_servicedescription(ASD_ServiceDescription asd_servicedescription) {
        this.asd_servicedescription = asd_servicedescription;
    }
    public List<ASD_Operation> getAsd_operations() {
        return asd_operations;
    }

    public void addAsd_operation(Asd_operation asd_operation) {
        this.asd_operations.add(asd_operation);
    }

}
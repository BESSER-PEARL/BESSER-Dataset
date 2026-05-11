





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregator extends DescriptionProvider, InfosProvider, StatusProvider {

    private String buildRoot;
    private boolean sendmail;
    private String type;
    private boolean mavenResult;
    private String label;
    private String packedStrategy;





    private List<aggregator_Contact> aggregator_contacts;




    private aggregator_Contact aggregator_contact;




    private List<aggregator_Contribution> aggregator_contributions;




    private List<aggregator_CustomCategory> aggregator_customcategorys;




    private aggregator_Contact aggregator_contact;




    private List<aggregator_Configuration> aggregator_configurations;


    public aggregator_Aggregator(
        String buildRoot,        boolean sendmail,        String type,        boolean mavenResult,        String label,        String packedStrategy    ) {
        super(
        );
        this.buildRoot = buildRoot;
        this.sendmail = sendmail;
        this.type = type;
        this.mavenResult = mavenResult;
        this.label = label;
        this.packedStrategy = packedStrategy;
        this.aggregator_contacts = new ArrayList<>();
        this.aggregator_contributions = new ArrayList<>();
        this.aggregator_customcategorys = new ArrayList<>();
        this.aggregator_configurations = new ArrayList<>();
    }

    public aggregator_Aggregator(
        String buildRoot,        boolean sendmail,        String type,        boolean mavenResult,        String label,        String packedStrategy        ArrayList<aggregator_Contact> aggregator_contacts,        ArrayList<aggregator_Contribution> aggregator_contributions,        ArrayList<aggregator_CustomCategory> aggregator_customcategorys,        ArrayList<aggregator_Configuration> aggregator_configurations    ) {
        this.buildRoot = buildRoot;
        this.sendmail = sendmail;
        this.type = type;
        this.mavenResult = mavenResult;
        this.label = label;
        this.packedStrategy = packedStrategy;
        this.aggregator_contacts = aggregator_contacts;
        this.aggregator_contributions = aggregator_contributions;
        this.aggregator_customcategorys = aggregator_customcategorys;
        this.aggregator_configurations = aggregator_configurations;
    }

    public String getBuildroot() {
        return buildRoot;
    }

    public void setBuildroot(String buildRoot) {
        this.buildRoot = buildRoot;
    }
    public boolean getSendmail() {
        return sendmail;
    }

    public void setSendmail(boolean sendmail) {
        this.sendmail = sendmail;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getMavenresult() {
        return mavenResult;
    }

    public void setMavenresult(boolean mavenResult) {
        this.mavenResult = mavenResult;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getPackedstrategy() {
        return packedStrategy;
    }

    public void setPackedstrategy(String packedStrategy) {
        this.packedStrategy = packedStrategy;
    }

    public List<aggregator_Contact> getAggregator_contacts() {
        return aggregator_contacts;
    }

    public void addAggregator_contact(Aggregator_contact aggregator_contact) {
        this.aggregator_contacts.add(aggregator_contact);
    }
    public aggregator_Contact getAggregator_contact() {
        return aggregator_contact;
    }

    public void setAggregator_contact(aggregator_Contact aggregator_contact) {
        this.aggregator_contact = aggregator_contact;
    }
    public List<aggregator_Contribution> getAggregator_contributions() {
        return aggregator_contributions;
    }

    public void addAggregator_contribution(Aggregator_contribution aggregator_contribution) {
        this.aggregator_contributions.add(aggregator_contribution);
    }
    public List<aggregator_CustomCategory> getAggregator_customcategorys() {
        return aggregator_customcategorys;
    }

    public void addAggregator_customcategory(Aggregator_customcategory aggregator_customcategory) {
        this.aggregator_customcategorys.add(aggregator_customcategory);
    }
    public aggregator_Contact getAggregator_contact() {
        return aggregator_contact;
    }

    public void setAggregator_contact(aggregator_Contact aggregator_contact) {
        this.aggregator_contact = aggregator_contact;
    }
    public List<aggregator_Configuration> getAggregator_configurations() {
        return aggregator_configurations;
    }

    public void addAggregator_configuration(Aggregator_configuration aggregator_configuration) {
        this.aggregator_configurations.add(aggregator_configuration);
    }

}
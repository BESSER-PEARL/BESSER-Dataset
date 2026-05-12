





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregator extends DescriptionProvider, InfosProvider, StatusProvider {

    private String packedStrategy;
    private String label;
    private String type;
    private boolean mavenResult;
    private boolean sendmail;
    private String buildRoot;





    private List<aggregator_Contact> aggregator_contacts;




    private aggregator_Contact aggregator_contact;




    private List<aggregator_Configuration> aggregator_configurations;




    private List<aggregator_Contribution> aggregator_contributions;




    private aggregator_Contact aggregator_contact;


    public aggregator_Aggregator(
        String packedStrategy,        String label,        String type,        boolean mavenResult,        boolean sendmail,        String buildRoot    ) {
        super(
        );
        this.packedStrategy = packedStrategy;
        this.label = label;
        this.type = type;
        this.mavenResult = mavenResult;
        this.sendmail = sendmail;
        this.buildRoot = buildRoot;
        this.aggregator_contacts = new ArrayList<>();
        this.aggregator_configurations = new ArrayList<>();
        this.aggregator_contributions = new ArrayList<>();
    }

    public aggregator_Aggregator(
        String packedStrategy,        String label,        String type,        boolean mavenResult,        boolean sendmail,        String buildRoot        ArrayList<aggregator_Contact> aggregator_contacts,        ArrayList<aggregator_Configuration> aggregator_configurations,        ArrayList<aggregator_Contribution> aggregator_contributions    ) {
        this.packedStrategy = packedStrategy;
        this.label = label;
        this.type = type;
        this.mavenResult = mavenResult;
        this.sendmail = sendmail;
        this.buildRoot = buildRoot;
        this.aggregator_contacts = aggregator_contacts;
        this.aggregator_configurations = aggregator_configurations;
        this.aggregator_contributions = aggregator_contributions;
    }

    public String getPackedstrategy() {
        return packedStrategy;
    }

    public void setPackedstrategy(String packedStrategy) {
        this.packedStrategy = packedStrategy;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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
    public boolean getSendmail() {
        return sendmail;
    }

    public void setSendmail(boolean sendmail) {
        this.sendmail = sendmail;
    }
    public String getBuildroot() {
        return buildRoot;
    }

    public void setBuildroot(String buildRoot) {
        this.buildRoot = buildRoot;
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
    public List<aggregator_Configuration> getAggregator_configurations() {
        return aggregator_configurations;
    }

    public void addAggregator_configuration(Aggregator_configuration aggregator_configuration) {
        this.aggregator_configurations.add(aggregator_configuration);
    }
    public List<aggregator_Contribution> getAggregator_contributions() {
        return aggregator_contributions;
    }

    public void addAggregator_contribution(Aggregator_contribution aggregator_contribution) {
        this.aggregator_contributions.add(aggregator_contribution);
    }
    public aggregator_Contact getAggregator_contact() {
        return aggregator_contact;
    }

    public void setAggregator_contact(aggregator_Contact aggregator_contact) {
        this.aggregator_contact = aggregator_contact;
    }

}
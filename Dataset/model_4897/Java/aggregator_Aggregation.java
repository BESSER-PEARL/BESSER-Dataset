





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregation extends StatusProvider, DescriptionProvider, InfosProvider {

    private String label;
    private boolean sendmail;
    private boolean mavenResult;
    private String type;
    private String packedStrategy;
    private String buildRoot;





    private aggregator_Contact aggregator_contact;




    private List<aggregator_CustomCategory> aggregator_customcategorys;




    private List<aggregator_Contact> aggregator_contacts;




    private aggregator_Contact aggregator_contact;


    public aggregator_Aggregation(
        String label,        boolean sendmail,        boolean mavenResult,        String type,        String packedStrategy,        String buildRoot    ) {
        super(
        );
        this.label = label;
        this.sendmail = sendmail;
        this.mavenResult = mavenResult;
        this.type = type;
        this.packedStrategy = packedStrategy;
        this.buildRoot = buildRoot;
        this.aggregator_customcategorys = new ArrayList<>();
        this.aggregator_contacts = new ArrayList<>();
    }

    public aggregator_Aggregation(
        String label,        boolean sendmail,        boolean mavenResult,        String type,        String packedStrategy,        String buildRoot        ArrayList<aggregator_CustomCategory> aggregator_customcategorys,        ArrayList<aggregator_Contact> aggregator_contacts    ) {
        this.label = label;
        this.sendmail = sendmail;
        this.mavenResult = mavenResult;
        this.type = type;
        this.packedStrategy = packedStrategy;
        this.buildRoot = buildRoot;
        this.aggregator_customcategorys = aggregator_customcategorys;
        this.aggregator_contacts = aggregator_contacts;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getSendmail() {
        return sendmail;
    }

    public void setSendmail(boolean sendmail) {
        this.sendmail = sendmail;
    }
    public boolean getMavenresult() {
        return mavenResult;
    }

    public void setMavenresult(boolean mavenResult) {
        this.mavenResult = mavenResult;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPackedstrategy() {
        return packedStrategy;
    }

    public void setPackedstrategy(String packedStrategy) {
        this.packedStrategy = packedStrategy;
    }
    public String getBuildroot() {
        return buildRoot;
    }

    public void setBuildroot(String buildRoot) {
        this.buildRoot = buildRoot;
    }

    public aggregator_Contact getAggregator_contact() {
        return aggregator_contact;
    }

    public void setAggregator_contact(aggregator_Contact aggregator_contact) {
        this.aggregator_contact = aggregator_contact;
    }
    public List<aggregator_CustomCategory> getAggregator_customcategorys() {
        return aggregator_customcategorys;
    }

    public void addAggregator_customcategory(Aggregator_customcategory aggregator_customcategory) {
        this.aggregator_customcategorys.add(aggregator_customcategory);
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

}
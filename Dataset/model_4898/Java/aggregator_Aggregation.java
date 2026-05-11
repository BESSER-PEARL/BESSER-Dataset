





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregation extends DescriptionProvider, StatusProvider, InfosProvider {

    private String label;
    private String type;
    private boolean strictMavenVersions;
    private String allowLegacySites;
    private boolean mavenResult;
    private boolean sendmail;
    private String packedStrategy;
    private String buildRoot;





    private List<aggregator_MavenMapping> aggregator_mavenmappings;




    private List<aggregator_ValidationSet> aggregator_validationsets;




    private List<aggregator_CustomCategory> aggregator_customcategorys;


    public aggregator_Aggregation(
        String label,        String type,        boolean strictMavenVersions,        String allowLegacySites,        boolean mavenResult,        boolean sendmail,        String packedStrategy,        String buildRoot    ) {
        super(
        );
        this.label = label;
        this.type = type;
        this.strictMavenVersions = strictMavenVersions;
        this.allowLegacySites = allowLegacySites;
        this.mavenResult = mavenResult;
        this.sendmail = sendmail;
        this.packedStrategy = packedStrategy;
        this.buildRoot = buildRoot;
        this.aggregator_mavenmappings = new ArrayList<>();
        this.aggregator_validationsets = new ArrayList<>();
        this.aggregator_customcategorys = new ArrayList<>();
    }

    public aggregator_Aggregation(
        String label,        String type,        boolean strictMavenVersions,        String allowLegacySites,        boolean mavenResult,        boolean sendmail,        String packedStrategy,        String buildRoot        ArrayList<aggregator_MavenMapping> aggregator_mavenmappings,        ArrayList<aggregator_ValidationSet> aggregator_validationsets,        ArrayList<aggregator_CustomCategory> aggregator_customcategorys    ) {
        this.label = label;
        this.type = type;
        this.strictMavenVersions = strictMavenVersions;
        this.allowLegacySites = allowLegacySites;
        this.mavenResult = mavenResult;
        this.sendmail = sendmail;
        this.packedStrategy = packedStrategy;
        this.buildRoot = buildRoot;
        this.aggregator_mavenmappings = aggregator_mavenmappings;
        this.aggregator_validationsets = aggregator_validationsets;
        this.aggregator_customcategorys = aggregator_customcategorys;
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
    public boolean getStrictmavenversions() {
        return strictMavenVersions;
    }

    public void setStrictmavenversions(boolean strictMavenVersions) {
        this.strictMavenVersions = strictMavenVersions;
    }
    public String getAllowlegacysites() {
        return allowLegacySites;
    }

    public void setAllowlegacysites(String allowLegacySites) {
        this.allowLegacySites = allowLegacySites;
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

    public List<aggregator_MavenMapping> getAggregator_mavenmappings() {
        return aggregator_mavenmappings;
    }

    public void addAggregator_mavenmapping(Aggregator_mavenmapping aggregator_mavenmapping) {
        this.aggregator_mavenmappings.add(aggregator_mavenmapping);
    }
    public List<aggregator_ValidationSet> getAggregator_validationsets() {
        return aggregator_validationsets;
    }

    public void addAggregator_validationset(Aggregator_validationset aggregator_validationset) {
        this.aggregator_validationsets.add(aggregator_validationset);
    }
    public List<aggregator_CustomCategory> getAggregator_customcategorys() {
        return aggregator_customcategorys;
    }

    public void addAggregator_customcategory(Aggregator_customcategory aggregator_customcategory) {
        this.aggregator_customcategorys.add(aggregator_customcategory);
    }

}
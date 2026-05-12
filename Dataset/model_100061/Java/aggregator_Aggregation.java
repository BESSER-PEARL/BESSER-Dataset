





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregation extends InfosProvider, StatusProvider, DescriptionProvider {

    private String allowLegacySites;
    private boolean strictMavenVersions;
    private String packedStrategy;
    private boolean sendmail;
    private boolean mavenResult;
    private String buildRoot;
    private String label;
    private String type;





    private List<aggregator_ValidationSet> aggregator_validationsets;




    private List<aggregator_CustomCategory> aggregator_customcategorys;


    public aggregator_Aggregation(
        String allowLegacySites,        boolean strictMavenVersions,        String packedStrategy,        boolean sendmail,        boolean mavenResult,        String buildRoot,        String label,        String type    ) {
        super(
        );
        this.allowLegacySites = allowLegacySites;
        this.strictMavenVersions = strictMavenVersions;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.mavenResult = mavenResult;
        this.buildRoot = buildRoot;
        this.label = label;
        this.type = type;
        this.aggregator_validationsets = new ArrayList<>();
        this.aggregator_customcategorys = new ArrayList<>();
    }

    public aggregator_Aggregation(
        String allowLegacySites,        boolean strictMavenVersions,        String packedStrategy,        boolean sendmail,        boolean mavenResult,        String buildRoot,        String label,        String type        ArrayList<aggregator_ValidationSet> aggregator_validationsets,        ArrayList<aggregator_CustomCategory> aggregator_customcategorys    ) {
        this.allowLegacySites = allowLegacySites;
        this.strictMavenVersions = strictMavenVersions;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.mavenResult = mavenResult;
        this.buildRoot = buildRoot;
        this.label = label;
        this.type = type;
        this.aggregator_validationsets = aggregator_validationsets;
        this.aggregator_customcategorys = aggregator_customcategorys;
    }

    public String getAllowlegacysites() {
        return allowLegacySites;
    }

    public void setAllowlegacysites(String allowLegacySites) {
        this.allowLegacySites = allowLegacySites;
    }
    public boolean getStrictmavenversions() {
        return strictMavenVersions;
    }

    public void setStrictmavenversions(boolean strictMavenVersions) {
        this.strictMavenVersions = strictMavenVersions;
    }
    public String getPackedstrategy() {
        return packedStrategy;
    }

    public void setPackedstrategy(String packedStrategy) {
        this.packedStrategy = packedStrategy;
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
    public String getBuildroot() {
        return buildRoot;
    }

    public void setBuildroot(String buildRoot) {
        this.buildRoot = buildRoot;
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
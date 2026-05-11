





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregation extends DescriptionProvider, StatusProvider, InfosProvider {

    private String versionFormat;
    private String label;
    private boolean strictMavenVersions;
    private String buildRoot;
    private String type;
    private boolean mavenResult;
    private String allowLegacySites;
    private String packedStrategy;
    private boolean sendmail;





    private List<aggregator_CustomCategory> aggregator_customcategorys;




    private List<aggregator_Configuration> aggregator_configurations;


    public aggregator_Aggregation(
        String versionFormat,        String label,        boolean strictMavenVersions,        String buildRoot,        String type,        boolean mavenResult,        String allowLegacySites,        String packedStrategy,        boolean sendmail    ) {
        super(
        );
        this.versionFormat = versionFormat;
        this.label = label;
        this.strictMavenVersions = strictMavenVersions;
        this.buildRoot = buildRoot;
        this.type = type;
        this.mavenResult = mavenResult;
        this.allowLegacySites = allowLegacySites;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.aggregator_customcategorys = new ArrayList<>();
        this.aggregator_configurations = new ArrayList<>();
    }

    public aggregator_Aggregation(
        String versionFormat,        String label,        boolean strictMavenVersions,        String buildRoot,        String type,        boolean mavenResult,        String allowLegacySites,        String packedStrategy,        boolean sendmail        ArrayList<aggregator_CustomCategory> aggregator_customcategorys,        ArrayList<aggregator_Configuration> aggregator_configurations    ) {
        this.versionFormat = versionFormat;
        this.label = label;
        this.strictMavenVersions = strictMavenVersions;
        this.buildRoot = buildRoot;
        this.type = type;
        this.mavenResult = mavenResult;
        this.allowLegacySites = allowLegacySites;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.aggregator_customcategorys = aggregator_customcategorys;
        this.aggregator_configurations = aggregator_configurations;
    }

    public String getVersionformat() {
        return versionFormat;
    }

    public void setVersionformat(String versionFormat) {
        this.versionFormat = versionFormat;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getStrictmavenversions() {
        return strictMavenVersions;
    }

    public void setStrictmavenversions(boolean strictMavenVersions) {
        this.strictMavenVersions = strictMavenVersions;
    }
    public String getBuildroot() {
        return buildRoot;
    }

    public void setBuildroot(String buildRoot) {
        this.buildRoot = buildRoot;
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
    public String getAllowlegacysites() {
        return allowLegacySites;
    }

    public void setAllowlegacysites(String allowLegacySites) {
        this.allowLegacySites = allowLegacySites;
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

    public List<aggregator_CustomCategory> getAggregator_customcategorys() {
        return aggregator_customcategorys;
    }

    public void addAggregator_customcategory(Aggregator_customcategory aggregator_customcategory) {
        this.aggregator_customcategorys.add(aggregator_customcategory);
    }
    public List<aggregator_Configuration> getAggregator_configurations() {
        return aggregator_configurations;
    }

    public void addAggregator_configuration(Aggregator_configuration aggregator_configuration) {
        this.aggregator_configurations.add(aggregator_configuration);
    }

}
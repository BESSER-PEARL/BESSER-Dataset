





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregator extends DescriptionProvider, InfosProvider, StatusProvider {

    private String label;
    private boolean sendmail;
    private String buildRoot;
    private boolean mavenResult;
    private String packedStrategy;
    private String type;





    private List<aggregator_Configuration> aggregator_configurations;




    private List<aggregator_MavenMapping> aggregator_mavenmappings;




    private List<aggregator_Contribution> aggregator_contributions;




    private List<aggregator_MetadataRepositoryReference> aggregator_metadatarepositoryreferences;




    private List<aggregator_CustomCategory> aggregator_customcategorys;


    public aggregator_Aggregator(
        String label,        boolean sendmail,        String buildRoot,        boolean mavenResult,        String packedStrategy,        String type    ) {
        super(
        );
        this.label = label;
        this.sendmail = sendmail;
        this.buildRoot = buildRoot;
        this.mavenResult = mavenResult;
        this.packedStrategy = packedStrategy;
        this.type = type;
        this.aggregator_configurations = new ArrayList<>();
        this.aggregator_mavenmappings = new ArrayList<>();
        this.aggregator_contributions = new ArrayList<>();
        this.aggregator_metadatarepositoryreferences = new ArrayList<>();
        this.aggregator_customcategorys = new ArrayList<>();
    }

    public aggregator_Aggregator(
        String label,        boolean sendmail,        String buildRoot,        boolean mavenResult,        String packedStrategy,        String type        ArrayList<aggregator_Configuration> aggregator_configurations,        ArrayList<aggregator_MavenMapping> aggregator_mavenmappings,        ArrayList<aggregator_Contribution> aggregator_contributions,        ArrayList<aggregator_MetadataRepositoryReference> aggregator_metadatarepositoryreferences,        ArrayList<aggregator_CustomCategory> aggregator_customcategorys    ) {
        this.label = label;
        this.sendmail = sendmail;
        this.buildRoot = buildRoot;
        this.mavenResult = mavenResult;
        this.packedStrategy = packedStrategy;
        this.type = type;
        this.aggregator_configurations = aggregator_configurations;
        this.aggregator_mavenmappings = aggregator_mavenmappings;
        this.aggregator_contributions = aggregator_contributions;
        this.aggregator_metadatarepositoryreferences = aggregator_metadatarepositoryreferences;
        this.aggregator_customcategorys = aggregator_customcategorys;
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
    public String getBuildroot() {
        return buildRoot;
    }

    public void setBuildroot(String buildRoot) {
        this.buildRoot = buildRoot;
    }
    public boolean getMavenresult() {
        return mavenResult;
    }

    public void setMavenresult(boolean mavenResult) {
        this.mavenResult = mavenResult;
    }
    public String getPackedstrategy() {
        return packedStrategy;
    }

    public void setPackedstrategy(String packedStrategy) {
        this.packedStrategy = packedStrategy;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<aggregator_Configuration> getAggregator_configurations() {
        return aggregator_configurations;
    }

    public void addAggregator_configuration(Aggregator_configuration aggregator_configuration) {
        this.aggregator_configurations.add(aggregator_configuration);
    }
    public List<aggregator_MavenMapping> getAggregator_mavenmappings() {
        return aggregator_mavenmappings;
    }

    public void addAggregator_mavenmapping(Aggregator_mavenmapping aggregator_mavenmapping) {
        this.aggregator_mavenmappings.add(aggregator_mavenmapping);
    }
    public List<aggregator_Contribution> getAggregator_contributions() {
        return aggregator_contributions;
    }

    public void addAggregator_contribution(Aggregator_contribution aggregator_contribution) {
        this.aggregator_contributions.add(aggregator_contribution);
    }
    public List<aggregator_MetadataRepositoryReference> getAggregator_metadatarepositoryreferences() {
        return aggregator_metadatarepositoryreferences;
    }

    public void addAggregator_metadatarepositoryreference(Aggregator_metadatarepositoryreference aggregator_metadatarepositoryreference) {
        this.aggregator_metadatarepositoryreferences.add(aggregator_metadatarepositoryreference);
    }
    public List<aggregator_CustomCategory> getAggregator_customcategorys() {
        return aggregator_customcategorys;
    }

    public void addAggregator_customcategory(Aggregator_customcategory aggregator_customcategory) {
        this.aggregator_customcategorys.add(aggregator_customcategory);
    }

}
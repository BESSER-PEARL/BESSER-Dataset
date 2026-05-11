





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregator extends StatusProvider, DescriptionProvider, InfosProvider {

    private String label;
    private boolean mavenResult;
    private String type;
    private String packedStrategy;
    private boolean sendmail;
    private String buildRoot;





    private List<aggregator_MetadataRepositoryReference> aggregator_metadatarepositoryreferences;


    public aggregator_Aggregator(
        String label,        boolean mavenResult,        String type,        String packedStrategy,        boolean sendmail,        String buildRoot    ) {
        super(
        );
        this.label = label;
        this.mavenResult = mavenResult;
        this.type = type;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.buildRoot = buildRoot;
        this.aggregator_metadatarepositoryreferences = new ArrayList<>();
    }

    public aggregator_Aggregator(
        String label,        boolean mavenResult,        String type,        String packedStrategy,        boolean sendmail,        String buildRoot        ArrayList<aggregator_MetadataRepositoryReference> aggregator_metadatarepositoryreferences    ) {
        this.label = label;
        this.mavenResult = mavenResult;
        this.type = type;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.buildRoot = buildRoot;
        this.aggregator_metadatarepositoryreferences = aggregator_metadatarepositoryreferences;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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

    public List<aggregator_MetadataRepositoryReference> getAggregator_metadatarepositoryreferences() {
        return aggregator_metadatarepositoryreferences;
    }

    public void addAggregator_metadatarepositoryreference(Aggregator_metadatarepositoryreference aggregator_metadatarepositoryreference) {
        this.aggregator_metadatarepositoryreferences.add(aggregator_metadatarepositoryreference);
    }

}
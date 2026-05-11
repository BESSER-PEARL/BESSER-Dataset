





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregator extends StatusProvider, DescriptionProvider, InfosProvider {

    private String buildRoot;
    private String label;
    private boolean mavenResult;
    private boolean sendmail;
    private String packedStrategy;
    private String type;





    private List<aggregator_Contribution> aggregator_contributions;




    private List<aggregator_Configuration> aggregator_configurations;


    public aggregator_Aggregator(
        String buildRoot,        String label,        boolean mavenResult,        boolean sendmail,        String packedStrategy,        String type    ) {
        super(
        );
        this.buildRoot = buildRoot;
        this.label = label;
        this.mavenResult = mavenResult;
        this.sendmail = sendmail;
        this.packedStrategy = packedStrategy;
        this.type = type;
        this.aggregator_contributions = new ArrayList<>();
        this.aggregator_configurations = new ArrayList<>();
    }

    public aggregator_Aggregator(
        String buildRoot,        String label,        boolean mavenResult,        boolean sendmail,        String packedStrategy,        String type        ArrayList<aggregator_Contribution> aggregator_contributions,        ArrayList<aggregator_Configuration> aggregator_configurations    ) {
        this.buildRoot = buildRoot;
        this.label = label;
        this.mavenResult = mavenResult;
        this.sendmail = sendmail;
        this.packedStrategy = packedStrategy;
        this.type = type;
        this.aggregator_contributions = aggregator_contributions;
        this.aggregator_configurations = aggregator_configurations;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<aggregator_Contribution> getAggregator_contributions() {
        return aggregator_contributions;
    }

    public void addAggregator_contribution(Aggregator_contribution aggregator_contribution) {
        this.aggregator_contributions.add(aggregator_contribution);
    }
    public List<aggregator_Configuration> getAggregator_configurations() {
        return aggregator_configurations;
    }

    public void addAggregator_configuration(Aggregator_configuration aggregator_configuration) {
        this.aggregator_configurations.add(aggregator_configuration);
    }

}
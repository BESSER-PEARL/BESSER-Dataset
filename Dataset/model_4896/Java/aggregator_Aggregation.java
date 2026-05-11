





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregation extends DescriptionProvider, InfosProvider, StatusProvider {

    private boolean mavenResult;
    private String label;
    private String buildRoot;
    private String type;
    private String packedStrategy;
    private boolean sendmail;





    private List<aggregator_ValidationSet> aggregator_validationsets;




    private List<aggregator_CustomCategory> aggregator_customcategorys;




    private List<aggregator_MavenMapping> aggregator_mavenmappings;


    public aggregator_Aggregation(
        boolean mavenResult,        String label,        String buildRoot,        String type,        String packedStrategy,        boolean sendmail    ) {
        super(
        );
        this.mavenResult = mavenResult;
        this.label = label;
        this.buildRoot = buildRoot;
        this.type = type;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.aggregator_validationsets = new ArrayList<>();
        this.aggregator_customcategorys = new ArrayList<>();
        this.aggregator_mavenmappings = new ArrayList<>();
    }

    public aggregator_Aggregation(
        boolean mavenResult,        String label,        String buildRoot,        String type,        String packedStrategy,        boolean sendmail        ArrayList<aggregator_ValidationSet> aggregator_validationsets,        ArrayList<aggregator_CustomCategory> aggregator_customcategorys,        ArrayList<aggregator_MavenMapping> aggregator_mavenmappings    ) {
        this.mavenResult = mavenResult;
        this.label = label;
        this.buildRoot = buildRoot;
        this.type = type;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.aggregator_validationsets = aggregator_validationsets;
        this.aggregator_customcategorys = aggregator_customcategorys;
        this.aggregator_mavenmappings = aggregator_mavenmappings;
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
    public List<aggregator_MavenMapping> getAggregator_mavenmappings() {
        return aggregator_mavenmappings;
    }

    public void addAggregator_mavenmapping(Aggregator_mavenmapping aggregator_mavenmapping) {
        this.aggregator_mavenmappings.add(aggregator_mavenmapping);
    }

}
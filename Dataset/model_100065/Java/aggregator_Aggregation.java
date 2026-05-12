





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregation extends InfosProvider, DescriptionProvider, StatusProvider {

    private boolean mavenResult;
    private String buildRoot;
    private String packedStrategy;
    private boolean sendmail;
    private String label;
    private String type;



    public aggregator_Aggregation(
        boolean mavenResult,        String buildRoot,        String packedStrategy,        boolean sendmail,        String label,        String type    ) {
        super(
        );
        this.mavenResult = mavenResult;
        this.buildRoot = buildRoot;
        this.packedStrategy = packedStrategy;
        this.sendmail = sendmail;
        this.label = label;
        this.type = type;
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


}
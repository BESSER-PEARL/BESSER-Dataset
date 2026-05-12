





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregator extends InfosProvider, StatusProvider, DescriptionProvider {

    private String buildRoot;
    private String type;
    private boolean sendmail;
    private String packedStrategy;
    private String label;
    private boolean mavenResult;



    public aggregator_Aggregator(
        String buildRoot,        String type,        boolean sendmail,        String packedStrategy,        String label,        boolean mavenResult    ) {
        super(
        );
        this.buildRoot = buildRoot;
        this.type = type;
        this.sendmail = sendmail;
        this.packedStrategy = packedStrategy;
        this.label = label;
        this.mavenResult = mavenResult;
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


}
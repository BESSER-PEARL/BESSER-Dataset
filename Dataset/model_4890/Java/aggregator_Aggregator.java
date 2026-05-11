





import java.util.List;
import java.util.ArrayList;

public class aggregator_Aggregator extends DescriptionProvider, InfosProvider, StatusProvider {

    private String packedStrategy;
    private String buildRoot;
    private String label;
    private String type;
    private boolean mavenResult;
    private boolean sendmail;



    public aggregator_Aggregator(
        String packedStrategy,        String buildRoot,        String label,        String type,        boolean mavenResult,        boolean sendmail    ) {
        super(
        );
        this.packedStrategy = packedStrategy;
        this.buildRoot = buildRoot;
        this.label = label;
        this.type = type;
        this.mavenResult = mavenResult;
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


}
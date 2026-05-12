





import java.util.List;
import java.util.ArrayList;

public class connection_SAPIDocUnit extends AbstractMetadataObject {

    private boolean useXmlOutput;
    private String xmlFile;
    private boolean useHtmlOutput;
    private String programId;
    private String htmlFile;
    private String gatewayService;



    public connection_SAPIDocUnit(
        boolean useXmlOutput,        String xmlFile,        boolean useHtmlOutput,        String programId,        String htmlFile,        String gatewayService    ) {
        super(
        );
        this.useXmlOutput = useXmlOutput;
        this.xmlFile = xmlFile;
        this.useHtmlOutput = useHtmlOutput;
        this.programId = programId;
        this.htmlFile = htmlFile;
        this.gatewayService = gatewayService;
    }


    public boolean getUsexmloutput() {
        return useXmlOutput;
    }

    public void setUsexmloutput(boolean useXmlOutput) {
        this.useXmlOutput = useXmlOutput;
    }
    public String getXmlfile() {
        return xmlFile;
    }

    public void setXmlfile(String xmlFile) {
        this.xmlFile = xmlFile;
    }
    public boolean getUsehtmloutput() {
        return useHtmlOutput;
    }

    public void setUsehtmloutput(boolean useHtmlOutput) {
        this.useHtmlOutput = useHtmlOutput;
    }
    public String getProgramid() {
        return programId;
    }

    public void setProgramid(String programId) {
        this.programId = programId;
    }
    public String getHtmlfile() {
        return htmlFile;
    }

    public void setHtmlfile(String htmlFile) {
        this.htmlFile = htmlFile;
    }
    public String getGatewayservice() {
        return gatewayService;
    }

    public void setGatewayservice(String gatewayService) {
        this.gatewayService = gatewayService;
    }


}
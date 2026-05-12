





import java.util.List;
import java.util.ArrayList;

public class connection_SAPIDocUnit extends AbstractMetadataObject {

    private String programId;
    private boolean useHtmlOutput;
    private boolean useXmlOutput;
    private String gatewayService;
    private String xmlFile;
    private String htmlFile;



    public connection_SAPIDocUnit(
        String programId,        boolean useHtmlOutput,        boolean useXmlOutput,        String gatewayService,        String xmlFile,        String htmlFile    ) {
        super(
        );
        this.programId = programId;
        this.useHtmlOutput = useHtmlOutput;
        this.useXmlOutput = useXmlOutput;
        this.gatewayService = gatewayService;
        this.xmlFile = xmlFile;
        this.htmlFile = htmlFile;
    }


    public String getProgramid() {
        return programId;
    }

    public void setProgramid(String programId) {
        this.programId = programId;
    }
    public boolean getUsehtmloutput() {
        return useHtmlOutput;
    }

    public void setUsehtmloutput(boolean useHtmlOutput) {
        this.useHtmlOutput = useHtmlOutput;
    }
    public boolean getUsexmloutput() {
        return useXmlOutput;
    }

    public void setUsexmloutput(boolean useXmlOutput) {
        this.useXmlOutput = useXmlOutput;
    }
    public String getGatewayservice() {
        return gatewayService;
    }

    public void setGatewayservice(String gatewayService) {
        this.gatewayService = gatewayService;
    }
    public String getXmlfile() {
        return xmlFile;
    }

    public void setXmlfile(String xmlFile) {
        this.xmlFile = xmlFile;
    }
    public String getHtmlfile() {
        return htmlFile;
    }

    public void setHtmlfile(String htmlFile) {
        this.htmlFile = htmlFile;
    }


}






import java.util.List;
import java.util.ArrayList;

public class connection_SAPIDocUnit extends AbstractMetadataObject {

    private String htmlFile;
    private boolean useHtmlOutput;
    private String gatewayService;
    private String programId;
    private boolean useXmlOutput;
    private String xmlFile;



    public connection_SAPIDocUnit(
        String htmlFile,        boolean useHtmlOutput,        String gatewayService,        String programId,        boolean useXmlOutput,        String xmlFile    ) {
        super(
        );
        this.htmlFile = htmlFile;
        this.useHtmlOutput = useHtmlOutput;
        this.gatewayService = gatewayService;
        this.programId = programId;
        this.useXmlOutput = useXmlOutput;
        this.xmlFile = xmlFile;
    }


    public String getHtmlfile() {
        return htmlFile;
    }

    public void setHtmlfile(String htmlFile) {
        this.htmlFile = htmlFile;
    }
    public boolean getUsehtmloutput() {
        return useHtmlOutput;
    }

    public void setUsehtmloutput(boolean useHtmlOutput) {
        this.useHtmlOutput = useHtmlOutput;
    }
    public String getGatewayservice() {
        return gatewayService;
    }

    public void setGatewayservice(String gatewayService) {
        this.gatewayService = gatewayService;
    }
    public String getProgramid() {
        return programId;
    }

    public void setProgramid(String programId) {
        this.programId = programId;
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


}
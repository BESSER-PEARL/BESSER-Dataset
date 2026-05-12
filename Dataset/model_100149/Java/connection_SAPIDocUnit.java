





import java.util.List;
import java.util.ArrayList;

public class connection_SAPIDocUnit extends AbstractMetadataObject {

    private String programId;
    private String gatewayService;
    private boolean useHtmlOutput;
    private String htmlFile;
    private String xmlFile;
    private boolean useXmlOutput;



    public connection_SAPIDocUnit(
        String programId,        String gatewayService,        boolean useHtmlOutput,        String htmlFile,        String xmlFile,        boolean useXmlOutput    ) {
        super(
        );
        this.programId = programId;
        this.gatewayService = gatewayService;
        this.useHtmlOutput = useHtmlOutput;
        this.htmlFile = htmlFile;
        this.xmlFile = xmlFile;
        this.useXmlOutput = useXmlOutput;
    }


    public String getProgramid() {
        return programId;
    }

    public void setProgramid(String programId) {
        this.programId = programId;
    }
    public String getGatewayservice() {
        return gatewayService;
    }

    public void setGatewayservice(String gatewayService) {
        this.gatewayService = gatewayService;
    }
    public boolean getUsehtmloutput() {
        return useHtmlOutput;
    }

    public void setUsehtmloutput(boolean useHtmlOutput) {
        this.useHtmlOutput = useHtmlOutput;
    }
    public String getHtmlfile() {
        return htmlFile;
    }

    public void setHtmlfile(String htmlFile) {
        this.htmlFile = htmlFile;
    }
    public String getXmlfile() {
        return xmlFile;
    }

    public void setXmlfile(String xmlFile) {
        this.xmlFile = xmlFile;
    }
    public boolean getUsexmloutput() {
        return useXmlOutput;
    }

    public void setUsexmloutput(boolean useXmlOutput) {
        this.useXmlOutput = useXmlOutput;
    }


}
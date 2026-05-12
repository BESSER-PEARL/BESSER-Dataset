





import java.util.List;
import java.util.ArrayList;

public class ptnet_ToolInfo  {

    private String version;
    private String tool;
    private String formattedXMLBuffer;
    private String toolInfoGrammarURI;



    public ptnet_ToolInfo(
        String version,        String tool,        String formattedXMLBuffer,        String toolInfoGrammarURI    ) {
        this.version = version;
        this.tool = tool;
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }
    public String getFormattedxmlbuffer() {
        return formattedXMLBuffer;
    }

    public void setFormattedxmlbuffer(String formattedXMLBuffer) {
        this.formattedXMLBuffer = formattedXMLBuffer;
    }
    public String getToolinfogrammaruri() {
        return toolInfoGrammarURI;
    }

    public void setToolinfogrammaruri(String toolInfoGrammarURI) {
        this.toolInfoGrammarURI = toolInfoGrammarURI;
    }


}






import java.util.List;
import java.util.ArrayList;

public class ptnet_ToolInfo  {

    private String version;
    private String tool;
    private String toolInfoGrammarURI;
    private String formattedXMLBuffer;



    public ptnet_ToolInfo(
        String version,        String tool,        String toolInfoGrammarURI,        String formattedXMLBuffer    ) {
        this.version = version;
        this.tool = tool;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.formattedXMLBuffer = formattedXMLBuffer;
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
    public String getToolinfogrammaruri() {
        return toolInfoGrammarURI;
    }

    public void setToolinfogrammaruri(String toolInfoGrammarURI) {
        this.toolInfoGrammarURI = toolInfoGrammarURI;
    }
    public String getFormattedxmlbuffer() {
        return formattedXMLBuffer;
    }

    public void setFormattedxmlbuffer(String formattedXMLBuffer) {
        this.formattedXMLBuffer = formattedXMLBuffer;
    }


}






import java.util.List;
import java.util.ArrayList;

public class ptnet_ToolInfo  {

    private String formattedXMLBuffer;
    private String version;
    private String toolInfoGrammarURI;
    private String tool;



    public ptnet_ToolInfo(
        String formattedXMLBuffer,        String version,        String toolInfoGrammarURI,        String tool    ) {
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.version = version;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.tool = tool;
    }


    public String getFormattedxmlbuffer() {
        return formattedXMLBuffer;
    }

    public void setFormattedxmlbuffer(String formattedXMLBuffer) {
        this.formattedXMLBuffer = formattedXMLBuffer;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getToolinfogrammaruri() {
        return toolInfoGrammarURI;
    }

    public void setToolinfogrammaruri(String toolInfoGrammarURI) {
        this.toolInfoGrammarURI = toolInfoGrammarURI;
    }
    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }


}






import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_ToolInfo  {

    private String toolInfoGrammarURI;
    private String tool;
    private String formattedXMLBuffer;
    private String version;



    public hlcorestructure_ToolInfo(
        String toolInfoGrammarURI,        String tool,        String formattedXMLBuffer,        String version    ) {
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.tool = tool;
        this.formattedXMLBuffer = formattedXMLBuffer;
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


}
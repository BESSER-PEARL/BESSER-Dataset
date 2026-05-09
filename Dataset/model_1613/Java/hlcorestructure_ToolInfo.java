





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_ToolInfo  {

    private String version;
    private String formattedXMLBuffer;
    private String tool;
    private String toolInfoGrammarURI;



    public hlcorestructure_ToolInfo(
        String version,        String formattedXMLBuffer,        String tool,        String toolInfoGrammarURI    ) {
        this.version = version;
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.tool = tool;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFormattedxmlbuffer() {
        return formattedXMLBuffer;
    }

    public void setFormattedxmlbuffer(String formattedXMLBuffer) {
        this.formattedXMLBuffer = formattedXMLBuffer;
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


}
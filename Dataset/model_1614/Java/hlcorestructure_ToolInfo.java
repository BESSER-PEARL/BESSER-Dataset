





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_ToolInfo  {

    private String formattedXMLBuffer;
    private String tool;
    private String version;
    private String toolInfoGrammarURI;



    public hlcorestructure_ToolInfo(
        String formattedXMLBuffer,        String tool,        String version,        String toolInfoGrammarURI    ) {
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.tool = tool;
        this.version = version;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
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


}
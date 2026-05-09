





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_ToolInfo  {

    private String tool;
    private String toolInfoGrammarURI;
    private String version;
    private String formattedXMLBuffer;



    public pnmlcoremodel_ToolInfo(
        String tool,        String toolInfoGrammarURI,        String version,        String formattedXMLBuffer    ) {
        this.tool = tool;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.version = version;
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


}
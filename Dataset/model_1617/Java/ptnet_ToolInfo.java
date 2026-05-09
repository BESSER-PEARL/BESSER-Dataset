





import java.util.List;
import java.util.ArrayList;

public class ptnet_ToolInfo  {

    private String tool;
    private String version;
    private String formattedXMLBuffer;
    private String toolInfoGrammarURI;





    private ptnet_PetriNet ptnet_petrinet;




    private ptnet_PetriNet ptnet_petrinet;


    public ptnet_ToolInfo(
        String tool,        String version,        String formattedXMLBuffer,        String toolInfoGrammarURI    ) {
        this.tool = tool;
        this.version = version;
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
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

    public ptnet_PetriNet getPtnet_petrinet() {
        return ptnet_petrinet;
    }

    public void setPtnet_petrinet(ptnet_PetriNet ptnet_petrinet) {
        this.ptnet_petrinet = ptnet_petrinet;
    }
    public ptnet_PetriNet getPtnet_petrinet() {
        return ptnet_petrinet;
    }

    public void setPtnet_petrinet(ptnet_PetriNet ptnet_petrinet) {
        this.ptnet_petrinet = ptnet_petrinet;
    }

}
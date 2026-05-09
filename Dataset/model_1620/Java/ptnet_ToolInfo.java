





import java.util.List;
import java.util.ArrayList;

public class ptnet_ToolInfo  {

    private String version;
    private String toolInfoGrammarURI;
    private String formattedXMLBuffer;
    private String tool;





    private ptnet_PetriNet ptnet_petrinet;




    private ptnet_PetriNet ptnet_petrinet;


    public ptnet_ToolInfo(
        String version,        String toolInfoGrammarURI,        String formattedXMLBuffer,        String tool    ) {
        this.version = version;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.formattedXMLBuffer = formattedXMLBuffer;
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
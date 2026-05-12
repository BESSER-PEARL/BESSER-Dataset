





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_ToolInfo  {

    private String formattedXMLBuffer;
    private String version;
    private String tool;
    private String toolInfoGrammarURI;





    private hlcorestructure_PetriNet hlcorestructure_petrinet;




    private hlcorestructure_PetriNet hlcorestructure_petrinet;


    public hlcorestructure_ToolInfo(
        String formattedXMLBuffer,        String version,        String tool,        String toolInfoGrammarURI    ) {
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.version = version;
        this.tool = tool;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
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

    public hlcorestructure_PetriNet getHlcorestructure_petrinet() {
        return hlcorestructure_petrinet;
    }

    public void setHlcorestructure_petrinet(hlcorestructure_PetriNet hlcorestructure_petrinet) {
        this.hlcorestructure_petrinet = hlcorestructure_petrinet;
    }
    public hlcorestructure_PetriNet getHlcorestructure_petrinet() {
        return hlcorestructure_petrinet;
    }

    public void setHlcorestructure_petrinet(hlcorestructure_PetriNet hlcorestructure_petrinet) {
        this.hlcorestructure_petrinet = hlcorestructure_petrinet;
    }

}
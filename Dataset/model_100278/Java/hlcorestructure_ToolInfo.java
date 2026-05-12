





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_ToolInfo  {

    private String version;
    private String toolInfoGrammarURI;
    private String tool;
    private String formattedXMLBuffer;





    private hlcorestructure_PnObject hlcorestructure_pnobject;




    private hlcorestructure_PetriNet hlcorestructure_petrinet;




    private hlcorestructure_PnObject hlcorestructure_pnobject;




    private hlcorestructure_PetriNet hlcorestructure_petrinet;


    public hlcorestructure_ToolInfo(
        String version,        String toolInfoGrammarURI,        String tool,        String formattedXMLBuffer    ) {
        this.version = version;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.tool = tool;
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
    public String getFormattedxmlbuffer() {
        return formattedXMLBuffer;
    }

    public void setFormattedxmlbuffer(String formattedXMLBuffer) {
        this.formattedXMLBuffer = formattedXMLBuffer;
    }

    public hlcorestructure_PnObject getHlcorestructure_pnobject() {
        return hlcorestructure_pnobject;
    }

    public void setHlcorestructure_pnobject(hlcorestructure_PnObject hlcorestructure_pnobject) {
        this.hlcorestructure_pnobject = hlcorestructure_pnobject;
    }
    public hlcorestructure_PetriNet getHlcorestructure_petrinet() {
        return hlcorestructure_petrinet;
    }

    public void setHlcorestructure_petrinet(hlcorestructure_PetriNet hlcorestructure_petrinet) {
        this.hlcorestructure_petrinet = hlcorestructure_petrinet;
    }
    public hlcorestructure_PnObject getHlcorestructure_pnobject() {
        return hlcorestructure_pnobject;
    }

    public void setHlcorestructure_pnobject(hlcorestructure_PnObject hlcorestructure_pnobject) {
        this.hlcorestructure_pnobject = hlcorestructure_pnobject;
    }
    public hlcorestructure_PetriNet getHlcorestructure_petrinet() {
        return hlcorestructure_petrinet;
    }

    public void setHlcorestructure_petrinet(hlcorestructure_PetriNet hlcorestructure_petrinet) {
        this.hlcorestructure_petrinet = hlcorestructure_petrinet;
    }

}
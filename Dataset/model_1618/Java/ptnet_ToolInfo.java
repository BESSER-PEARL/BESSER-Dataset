





import java.util.List;
import java.util.ArrayList;

public class ptnet_ToolInfo  {

    private String formattedXMLBuffer;
    private String toolInfoGrammarURI;
    private String tool;
    private String version;





    private ptnet_PetriNet ptnet_petrinet;




    private ptnet_PetriNet ptnet_petrinet;




    private ptnet_PnObject ptnet_pnobject;




    private ptnet_PnObject ptnet_pnobject;


    public ptnet_ToolInfo(
        String formattedXMLBuffer,        String toolInfoGrammarURI,        String tool,        String version    ) {
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.tool = tool;
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
    public ptnet_PnObject getPtnet_pnobject() {
        return ptnet_pnobject;
    }

    public void setPtnet_pnobject(ptnet_PnObject ptnet_pnobject) {
        this.ptnet_pnobject = ptnet_pnobject;
    }
    public ptnet_PnObject getPtnet_pnobject() {
        return ptnet_pnobject;
    }

    public void setPtnet_pnobject(ptnet_PnObject ptnet_pnobject) {
        this.ptnet_pnobject = ptnet_pnobject;
    }

}
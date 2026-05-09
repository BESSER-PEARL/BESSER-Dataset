





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_ToolInfo  {

    private String formattedXMLBuffer;
    private String toolInfoGrammarURI;
    private String version;
    private String tool;





    private pnmlcoremodel_PetriNet pnmlcoremodel_petrinet;




    private pnmlcoremodel_PetriNet pnmlcoremodel_petrinet;


    public pnmlcoremodel_ToolInfo(
        String formattedXMLBuffer,        String toolInfoGrammarURI,        String version,        String tool    ) {
        this.formattedXMLBuffer = formattedXMLBuffer;
        this.toolInfoGrammarURI = toolInfoGrammarURI;
        this.version = version;
        this.tool = tool;
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

    public pnmlcoremodel_PetriNet getPnmlcoremodel_petrinet() {
        return pnmlcoremodel_petrinet;
    }

    public void setPnmlcoremodel_petrinet(pnmlcoremodel_PetriNet pnmlcoremodel_petrinet) {
        this.pnmlcoremodel_petrinet = pnmlcoremodel_petrinet;
    }
    public pnmlcoremodel_PetriNet getPnmlcoremodel_petrinet() {
        return pnmlcoremodel_petrinet;
    }

    public void setPnmlcoremodel_petrinet(pnmlcoremodel_PetriNet pnmlcoremodel_petrinet) {
        this.pnmlcoremodel_petrinet = pnmlcoremodel_petrinet;
    }

}
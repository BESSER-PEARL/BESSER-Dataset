





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_ToolInfo  {

    private String version;
    private String tool;





    private pnmlcoremodel_Object pnmlcoremodel_object;




    private pnmlcoremodel_PetriNet pnmlcoremodel_petrinet;


    public pnmlcoremodel_ToolInfo(
        String version,        String tool    ) {
        this.version = version;
        this.tool = tool;
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

    public pnmlcoremodel_Object getPnmlcoremodel_object() {
        return pnmlcoremodel_object;
    }

    public void setPnmlcoremodel_object(pnmlcoremodel_Object pnmlcoremodel_object) {
        this.pnmlcoremodel_object = pnmlcoremodel_object;
    }
    public pnmlcoremodel_PetriNet getPnmlcoremodel_petrinet() {
        return pnmlcoremodel_petrinet;
    }

    public void setPnmlcoremodel_petrinet(pnmlcoremodel_PetriNet pnmlcoremodel_petrinet) {
        this.pnmlcoremodel_petrinet = pnmlcoremodel_petrinet;
    }

}
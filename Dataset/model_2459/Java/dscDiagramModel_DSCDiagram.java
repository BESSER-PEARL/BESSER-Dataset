





import java.util.List;
import java.util.ArrayList;

public class dscDiagramModel_DSCDiagram extends GenericDiagram {

    private String guardFile;
    private String actionFile;
    private String functionFile;
    private String eventFile;
    private String diagramVariables;



    public dscDiagramModel_DSCDiagram(
        String guardFile,        String actionFile,        String functionFile,        String eventFile,        String diagramVariables    ) {
        super(
        );
        this.guardFile = guardFile;
        this.actionFile = actionFile;
        this.functionFile = functionFile;
        this.eventFile = eventFile;
        this.diagramVariables = diagramVariables;
    }


    public String getGuardfile() {
        return guardFile;
    }

    public void setGuardfile(String guardFile) {
        this.guardFile = guardFile;
    }
    public String getActionfile() {
        return actionFile;
    }

    public void setActionfile(String actionFile) {
        this.actionFile = actionFile;
    }
    public String getFunctionfile() {
        return functionFile;
    }

    public void setFunctionfile(String functionFile) {
        this.functionFile = functionFile;
    }
    public String getEventfile() {
        return eventFile;
    }

    public void setEventfile(String eventFile) {
        this.eventFile = eventFile;
    }
    public String getDiagramvariables() {
        return diagramVariables;
    }

    public void setDiagramvariables(String diagramVariables) {
        this.diagramVariables = diagramVariables;
    }


}
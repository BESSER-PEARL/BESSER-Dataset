





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysisSessionEObject  {

    private String synchronizationStatus;
    private String resources;
    private String controlledResources;
    private boolean open;





    private viewpoint_SessionManagerEObject viewpoint_sessionmanagereobject;




    private List<viewpoint_DAnalysis> viewpoint_danalysiss;




    private List<Viewpoint> viewpoints;


    public viewpoint_DAnalysisSessionEObject(
        String synchronizationStatus,        String resources,        String controlledResources,        boolean open    ) {
        this.synchronizationStatus = synchronizationStatus;
        this.resources = resources;
        this.controlledResources = controlledResources;
        this.open = open;
        this.viewpoint_danalysiss = new ArrayList<>();
        this.viewpoints = new ArrayList<>();
    }

    public viewpoint_DAnalysisSessionEObject(
        String synchronizationStatus,        String resources,        String controlledResources,        boolean open        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss,        ArrayList<Viewpoint> viewpoints    ) {
        this.synchronizationStatus = synchronizationStatus;
        this.resources = resources;
        this.controlledResources = controlledResources;
        this.open = open;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
        this.viewpoints = viewpoints;
    }

    public String getSynchronizationstatus() {
        return synchronizationStatus;
    }

    public void setSynchronizationstatus(String synchronizationStatus) {
        this.synchronizationStatus = synchronizationStatus;
    }
    public String getResources() {
        return resources;
    }

    public void setResources(String resources) {
        this.resources = resources;
    }
    public String getControlledresources() {
        return controlledResources;
    }

    public void setControlledresources(String controlledResources) {
        this.controlledResources = controlledResources;
    }
    public boolean getOpen() {
        return open;
    }

    public void setOpen(boolean open) {
        this.open = open;
    }

    public viewpoint_SessionManagerEObject getViewpoint_sessionmanagereobject() {
        return viewpoint_sessionmanagereobject;
    }

    public void setViewpoint_sessionmanagereobject(viewpoint_SessionManagerEObject viewpoint_sessionmanagereobject) {
        this.viewpoint_sessionmanagereobject = viewpoint_sessionmanagereobject;
    }
    public List<viewpoint_DAnalysis> getViewpoint_danalysiss() {
        return viewpoint_danalysiss;
    }

    public void addViewpoint_danalysis(Viewpoint_danalysis viewpoint_danalysis) {
        this.viewpoint_danalysiss.add(viewpoint_danalysis);
    }
    public List<Viewpoint> getViewpoints() {
        return viewpoints;
    }

    public void addViewpoint(Viewpoint viewpoint) {
        this.viewpoints.add(viewpoint);
    }

}






import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysisSessionEObject  {

    private boolean open;
    private String synchronizationStatus;
    private String controlledResources;
    private String resources;





    private List<Viewpoint> viewpoints;




    private List<viewpoint_DAnalysis> viewpoint_danalysiss;




    private viewpoint_SessionManagerEObject viewpoint_sessionmanagereobject;


    public viewpoint_DAnalysisSessionEObject(
        boolean open,        String synchronizationStatus,        String controlledResources,        String resources    ) {
        this.open = open;
        this.synchronizationStatus = synchronizationStatus;
        this.controlledResources = controlledResources;
        this.resources = resources;
        this.viewpoints = new ArrayList<>();
        this.viewpoint_danalysiss = new ArrayList<>();
    }

    public viewpoint_DAnalysisSessionEObject(
        boolean open,        String synchronizationStatus,        String controlledResources,        String resources        ArrayList<Viewpoint> viewpoints,        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss    ) {
        this.open = open;
        this.synchronizationStatus = synchronizationStatus;
        this.controlledResources = controlledResources;
        this.resources = resources;
        this.viewpoints = viewpoints;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
    }

    public boolean getOpen() {
        return open;
    }

    public void setOpen(boolean open) {
        this.open = open;
    }
    public String getSynchronizationstatus() {
        return synchronizationStatus;
    }

    public void setSynchronizationstatus(String synchronizationStatus) {
        this.synchronizationStatus = synchronizationStatus;
    }
    public String getControlledresources() {
        return controlledResources;
    }

    public void setControlledresources(String controlledResources) {
        this.controlledResources = controlledResources;
    }
    public String getResources() {
        return resources;
    }

    public void setResources(String resources) {
        this.resources = resources;
    }

    public List<Viewpoint> getViewpoints() {
        return viewpoints;
    }

    public void addViewpoint(Viewpoint viewpoint) {
        this.viewpoints.add(viewpoint);
    }
    public List<viewpoint_DAnalysis> getViewpoint_danalysiss() {
        return viewpoint_danalysiss;
    }

    public void addViewpoint_danalysis(Viewpoint_danalysis viewpoint_danalysis) {
        this.viewpoint_danalysiss.add(viewpoint_danalysis);
    }
    public viewpoint_SessionManagerEObject getViewpoint_sessionmanagereobject() {
        return viewpoint_sessionmanagereobject;
    }

    public void setViewpoint_sessionmanagereobject(viewpoint_SessionManagerEObject viewpoint_sessionmanagereobject) {
        this.viewpoint_sessionmanagereobject = viewpoint_sessionmanagereobject;
    }

}
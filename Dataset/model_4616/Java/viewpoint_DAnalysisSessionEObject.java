





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysisSessionEObject  {

    private boolean open;
    private String resources;
    private boolean blocked;
    private String synchronizationStatus;
    private String controlledResources;





    private viewpoint_SessionManagerEObject viewpoint_sessionmanagereobject;




    private List<viewpoint_DAnalysis> viewpoint_danalysiss;




    private List<Viewpoint> viewpoints;


    public viewpoint_DAnalysisSessionEObject(
        boolean open,        String resources,        boolean blocked,        String synchronizationStatus,        String controlledResources    ) {
        this.open = open;
        this.resources = resources;
        this.blocked = blocked;
        this.synchronizationStatus = synchronizationStatus;
        this.controlledResources = controlledResources;
        this.viewpoint_danalysiss = new ArrayList<>();
        this.viewpoints = new ArrayList<>();
    }

    public viewpoint_DAnalysisSessionEObject(
        boolean open,        String resources,        boolean blocked,        String synchronizationStatus,        String controlledResources        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss,        ArrayList<Viewpoint> viewpoints    ) {
        this.open = open;
        this.resources = resources;
        this.blocked = blocked;
        this.synchronizationStatus = synchronizationStatus;
        this.controlledResources = controlledResources;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
        this.viewpoints = viewpoints;
    }

    public boolean getOpen() {
        return open;
    }

    public void setOpen(boolean open) {
        this.open = open;
    }
    public String getResources() {
        return resources;
    }

    public void setResources(String resources) {
        this.resources = resources;
    }
    public boolean getBlocked() {
        return blocked;
    }

    public void setBlocked(boolean blocked) {
        this.blocked = blocked;
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
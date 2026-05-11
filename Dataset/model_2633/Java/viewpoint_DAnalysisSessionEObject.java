





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysisSessionEObject  {

    private String resources;
    private boolean blocked;
    private boolean open;
    private String controlledResources;
    private String synchronizationStatus;





    private List<viewpoint_DAnalysis> viewpoint_danalysiss;




    private List<Viewpoint> viewpoints;


    public viewpoint_DAnalysisSessionEObject(
        String resources,        boolean blocked,        boolean open,        String controlledResources,        String synchronizationStatus    ) {
        this.resources = resources;
        this.blocked = blocked;
        this.open = open;
        this.controlledResources = controlledResources;
        this.synchronizationStatus = synchronizationStatus;
        this.viewpoint_danalysiss = new ArrayList<>();
        this.viewpoints = new ArrayList<>();
    }

    public viewpoint_DAnalysisSessionEObject(
        String resources,        boolean blocked,        boolean open,        String controlledResources,        String synchronizationStatus        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss,        ArrayList<Viewpoint> viewpoints    ) {
        this.resources = resources;
        this.blocked = blocked;
        this.open = open;
        this.controlledResources = controlledResources;
        this.synchronizationStatus = synchronizationStatus;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
        this.viewpoints = viewpoints;
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
    public boolean getOpen() {
        return open;
    }

    public void setOpen(boolean open) {
        this.open = open;
    }
    public String getControlledresources() {
        return controlledResources;
    }

    public void setControlledresources(String controlledResources) {
        this.controlledResources = controlledResources;
    }
    public String getSynchronizationstatus() {
        return synchronizationStatus;
    }

    public void setSynchronizationstatus(String synchronizationStatus) {
        this.synchronizationStatus = synchronizationStatus;
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






import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysisSessionEObject  {

    private String resources;
    private String synchronizationStatus;
    private boolean open;
    private String controlledResources;





    private List<viewpoint_DAnalysis> viewpoint_danalysiss;




    private List<Viewpoint> viewpoints;


    public viewpoint_DAnalysisSessionEObject(
        String resources,        String synchronizationStatus,        boolean open,        String controlledResources    ) {
        this.resources = resources;
        this.synchronizationStatus = synchronizationStatus;
        this.open = open;
        this.controlledResources = controlledResources;
        this.viewpoint_danalysiss = new ArrayList<>();
        this.viewpoints = new ArrayList<>();
    }

    public viewpoint_DAnalysisSessionEObject(
        String resources,        String synchronizationStatus,        boolean open,        String controlledResources        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss,        ArrayList<Viewpoint> viewpoints    ) {
        this.resources = resources;
        this.synchronizationStatus = synchronizationStatus;
        this.open = open;
        this.controlledResources = controlledResources;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
        this.viewpoints = viewpoints;
    }

    public String getResources() {
        return resources;
    }

    public void setResources(String resources) {
        this.resources = resources;
    }
    public String getSynchronizationstatus() {
        return synchronizationStatus;
    }

    public void setSynchronizationstatus(String synchronizationStatus) {
        this.synchronizationStatus = synchronizationStatus;
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
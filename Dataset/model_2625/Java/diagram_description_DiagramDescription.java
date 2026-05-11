





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramDescription extends description_DragAndDropTargetDescription, description_RepresentationDescription, description_PasteTargetDescription {

    private String domainClass;
    private String preconditionExpression;
    private boolean enablePopupBars;
    private String rootExpression;





    private concern_ConcernDescription concern_concerndescription;




    private List<ContainerMapping> containermappings;




    private List<DiagramElementMapping> diagramelementmappings;




    private List<NodeMapping> nodemappings;




    private List<ContainerMapping> containermappings;




    private List<NodeMapping> nodemappings;




    private Layer layer;




    private List<filter_FilterDescription> filter_filterdescriptions;




    private List<Layer> layers;


    public diagram_description_DiagramDescription(
        String domainClass,        String preconditionExpression,        boolean enablePopupBars,        String rootExpression    ) {
        super(
        );
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.enablePopupBars = enablePopupBars;
        this.rootExpression = rootExpression;
        this.containermappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.filter_filterdescriptions = new ArrayList<>();
        this.layers = new ArrayList<>();
    }

    public diagram_description_DiagramDescription(
        String domainClass,        String preconditionExpression,        boolean enablePopupBars,        String rootExpression        ArrayList<ContainerMapping> containermappings,        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<ContainerMapping> containermappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<filter_FilterDescription> filter_filterdescriptions,        ArrayList<Layer> layers    ) {
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.enablePopupBars = enablePopupBars;
        this.rootExpression = rootExpression;
        this.containermappings = containermappings;
        this.diagramelementmappings = diagramelementmappings;
        this.nodemappings = nodemappings;
        this.containermappings = containermappings;
        this.nodemappings = nodemappings;
        this.filter_filterdescriptions = filter_filterdescriptions;
        this.layers = layers;
    }

    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public boolean getEnablepopupbars() {
        return enablePopupBars;
    }

    public void setEnablepopupbars(boolean enablePopupBars) {
        this.enablePopupBars = enablePopupBars;
    }
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
    }

    public concern_ConcernDescription getConcern_concerndescription() {
        return concern_concerndescription;
    }

    public void setConcern_concerndescription(concern_ConcernDescription concern_concerndescription) {
        this.concern_concerndescription = concern_concerndescription;
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public Layer getLayer() {
        return layer;
    }

    public void setLayer(Layer layer) {
        this.layer = layer;
    }
    public List<filter_FilterDescription> getFilter_filterdescriptions() {
        return filter_filterdescriptions;
    }

    public void addFilter_filterdescription(Filter_filterdescription filter_filterdescription) {
        this.filter_filterdescriptions.add(filter_filterdescription);
    }
    public List<Layer> getLayers() {
        return layers;
    }

    public void addLayer(Layer layer) {
        this.layers.add(layer);
    }

}
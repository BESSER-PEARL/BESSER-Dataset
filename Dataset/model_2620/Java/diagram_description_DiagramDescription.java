





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramDescription extends description_DragAndDropTargetDescription, description_PasteTargetDescription, description_RepresentationDescription {

    private String rootExpression;
    private boolean enablePopupBars;
    private String preconditionExpression;
    private String domainClass;





    private List<ContainerMapping> containermappings;




    private List<NodeMapping> nodemappings;




    private List<NodeMapping> nodemappings;




    private List<DiagramElementMapping> diagramelementmappings;




    private List<filter_FilterDescription> filter_filterdescriptions;




    private concern_ConcernDescription concern_concerndescription;




    private Layer layer;




    private List<Layer> layers;




    private List<ContainerMapping> containermappings;


    public diagram_description_DiagramDescription(
        String rootExpression,        boolean enablePopupBars,        String preconditionExpression,        String domainClass    ) {
        super(
        );
        this.rootExpression = rootExpression;
        this.enablePopupBars = enablePopupBars;
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.containermappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
        this.filter_filterdescriptions = new ArrayList<>();
        this.layers = new ArrayList<>();
        this.containermappings = new ArrayList<>();
    }

    public diagram_description_DiagramDescription(
        String rootExpression,        boolean enablePopupBars,        String preconditionExpression,        String domainClass        ArrayList<ContainerMapping> containermappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<filter_FilterDescription> filter_filterdescriptions,        ArrayList<Layer> layers,        ArrayList<ContainerMapping> containermappings    ) {
        this.rootExpression = rootExpression;
        this.enablePopupBars = enablePopupBars;
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.containermappings = containermappings;
        this.nodemappings = nodemappings;
        this.nodemappings = nodemappings;
        this.diagramelementmappings = diagramelementmappings;
        this.filter_filterdescriptions = filter_filterdescriptions;
        this.layers = layers;
        this.containermappings = containermappings;
    }

    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
    }
    public boolean getEnablepopupbars() {
        return enablePopupBars;
    }

    public void setEnablepopupbars(boolean enablePopupBars) {
        this.enablePopupBars = enablePopupBars;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
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
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }
    public List<filter_FilterDescription> getFilter_filterdescriptions() {
        return filter_filterdescriptions;
    }

    public void addFilter_filterdescription(Filter_filterdescription filter_filterdescription) {
        this.filter_filterdescriptions.add(filter_filterdescription);
    }
    public concern_ConcernDescription getConcern_concerndescription() {
        return concern_concerndescription;
    }

    public void setConcern_concerndescription(concern_ConcernDescription concern_concerndescription) {
        this.concern_concerndescription = concern_concerndescription;
    }
    public Layer getLayer() {
        return layer;
    }

    public void setLayer(Layer layer) {
        this.layer = layer;
    }
    public List<Layer> getLayers() {
        return layers;
    }

    public void addLayer(Layer layer) {
        this.layers.add(layer);
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }

}
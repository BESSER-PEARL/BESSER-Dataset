





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramDescription extends description_RepresentationDescription, description_DragAndDropTargetDescription, description_PasteTargetDescription {

    private String preconditionExpression;
    private String rootExpression;
    private boolean enablePopupBars;
    private String domainClass;





    private Layer layer;




    private List<NodeMapping> nodemappings;




    private List<Layer> layers;




    private List<DiagramElementMapping> diagramelementmappings;




    private concern_ConcernDescription concern_concerndescription;




    private List<ContainerMapping> containermappings;




    private List<NodeMapping> nodemappings;




    private List<filter_FilterDescription> filter_filterdescriptions;




    private List<ContainerMapping> containermappings;


    public diagram_description_DiagramDescription(
        String preconditionExpression,        String rootExpression,        boolean enablePopupBars,        String domainClass    ) {
        super(
        );
        this.preconditionExpression = preconditionExpression;
        this.rootExpression = rootExpression;
        this.enablePopupBars = enablePopupBars;
        this.domainClass = domainClass;
        this.nodemappings = new ArrayList<>();
        this.layers = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.filter_filterdescriptions = new ArrayList<>();
        this.containermappings = new ArrayList<>();
    }

    public diagram_description_DiagramDescription(
        String preconditionExpression,        String rootExpression,        boolean enablePopupBars,        String domainClass        ArrayList<NodeMapping> nodemappings,        ArrayList<Layer> layers,        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<ContainerMapping> containermappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<filter_FilterDescription> filter_filterdescriptions,        ArrayList<ContainerMapping> containermappings    ) {
        this.preconditionExpression = preconditionExpression;
        this.rootExpression = rootExpression;
        this.enablePopupBars = enablePopupBars;
        this.domainClass = domainClass;
        this.nodemappings = nodemappings;
        this.layers = layers;
        this.diagramelementmappings = diagramelementmappings;
        this.containermappings = containermappings;
        this.nodemappings = nodemappings;
        this.filter_filterdescriptions = filter_filterdescriptions;
        this.containermappings = containermappings;
    }

    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
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
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }

    public Layer getLayer() {
        return layer;
    }

    public void setLayer(Layer layer) {
        this.layer = layer;
    }
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<Layer> getLayers() {
        return layers;
    }

    public void addLayer(Layer layer) {
        this.layers.add(layer);
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
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
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<filter_FilterDescription> getFilter_filterdescriptions() {
        return filter_filterdescriptions;
    }

    public void addFilter_filterdescription(Filter_filterdescription filter_filterdescription) {
        this.filter_filterdescriptions.add(filter_filterdescription);
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }

}
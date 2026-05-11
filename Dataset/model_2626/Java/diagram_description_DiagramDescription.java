





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramDescription extends description_DragAndDropTargetDescription, description_PasteTargetDescription, description_RepresentationDescription {

    private boolean enablePopupBars;
    private String preconditionExpression;
    private String domainClass;
    private String rootExpression;





    private List<NodeMapping> nodemappings;




    private List<Layer> layers;




    private List<filter_FilterDescription> filter_filterdescriptions;




    private List<DiagramElementMapping> diagramelementmappings;




    private List<ContainerMapping> containermappings;




    private List<AdditionalLayer> additionallayers;




    private concern_ConcernDescription concern_concerndescription;




    private List<ContainerMapping> containermappings;




    private List<NodeMapping> nodemappings;




    private Layer layer;


    public diagram_description_DiagramDescription(
        boolean enablePopupBars,        String preconditionExpression,        String domainClass,        String rootExpression    ) {
        super(
        );
        this.enablePopupBars = enablePopupBars;
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.rootExpression = rootExpression;
        this.nodemappings = new ArrayList<>();
        this.layers = new ArrayList<>();
        this.filter_filterdescriptions = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.additionallayers = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
    }

    public diagram_description_DiagramDescription(
        boolean enablePopupBars,        String preconditionExpression,        String domainClass,        String rootExpression        ArrayList<NodeMapping> nodemappings,        ArrayList<Layer> layers,        ArrayList<filter_FilterDescription> filter_filterdescriptions,        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<ContainerMapping> containermappings,        ArrayList<AdditionalLayer> additionallayers,        ArrayList<ContainerMapping> containermappings,        ArrayList<NodeMapping> nodemappings    ) {
        this.enablePopupBars = enablePopupBars;
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.rootExpression = rootExpression;
        this.nodemappings = nodemappings;
        this.layers = layers;
        this.filter_filterdescriptions = filter_filterdescriptions;
        this.diagramelementmappings = diagramelementmappings;
        this.containermappings = containermappings;
        this.additionallayers = additionallayers;
        this.containermappings = containermappings;
        this.nodemappings = nodemappings;
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
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
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
    public List<filter_FilterDescription> getFilter_filterdescriptions() {
        return filter_filterdescriptions;
    }

    public void addFilter_filterdescription(Filter_filterdescription filter_filterdescription) {
        this.filter_filterdescriptions.add(filter_filterdescription);
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }
    public List<AdditionalLayer> getAdditionallayers() {
        return additionallayers;
    }

    public void addAdditionallayer(Additionallayer additionallayer) {
        this.additionallayers.add(additionallayer);
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
    public Layer getLayer() {
        return layer;
    }

    public void setLayer(Layer layer) {
        this.layer = layer;
    }

}
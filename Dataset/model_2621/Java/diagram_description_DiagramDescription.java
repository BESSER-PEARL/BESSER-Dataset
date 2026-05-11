





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramDescription extends description_DragAndDropTargetDescription, description_PasteTargetDescription, description_RepresentationDescription {

    private String domainClass;
    private String preconditionExpression;
    private boolean enablePopupBars;
    private String rootExpression;





    private List<DiagramElementMapping> diagramelementmappings;




    private List<filter_FilterDescription> filter_filterdescriptions;




    private List<NodeMapping> nodemappings;




    private List<AdditionalLayer> additionallayers;




    private List<ContainerMapping> containermappings;




    private concern_ConcernDescription concern_concerndescription;




    private Layer layer;


    public diagram_description_DiagramDescription(
        String domainClass,        String preconditionExpression,        boolean enablePopupBars,        String rootExpression    ) {
        super(
        );
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.enablePopupBars = enablePopupBars;
        this.rootExpression = rootExpression;
        this.diagramelementmappings = new ArrayList<>();
        this.filter_filterdescriptions = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.additionallayers = new ArrayList<>();
        this.containermappings = new ArrayList<>();
    }

    public diagram_description_DiagramDescription(
        String domainClass,        String preconditionExpression,        boolean enablePopupBars,        String rootExpression        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<filter_FilterDescription> filter_filterdescriptions,        ArrayList<NodeMapping> nodemappings,        ArrayList<AdditionalLayer> additionallayers,        ArrayList<ContainerMapping> containermappings    ) {
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.enablePopupBars = enablePopupBars;
        this.rootExpression = rootExpression;
        this.diagramelementmappings = diagramelementmappings;
        this.filter_filterdescriptions = filter_filterdescriptions;
        this.nodemappings = nodemappings;
        this.additionallayers = additionallayers;
        this.containermappings = containermappings;
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
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<AdditionalLayer> getAdditionallayers() {
        return additionallayers;
    }

    public void addAdditionallayer(Additionallayer additionallayer) {
        this.additionallayers.add(additionallayer);
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
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

}
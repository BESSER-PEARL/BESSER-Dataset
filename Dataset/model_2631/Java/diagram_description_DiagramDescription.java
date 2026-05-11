





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramDescription extends description_PasteTargetDescription, description_RepresentationDescription, description_DragAndDropTargetDescription {

    private String rootExpression;
    private String preconditionExpression;
    private boolean enablePopupBars;
    private String domainClass;





    private List<Layer> layers;




    private concern_ConcernDescription concern_concerndescription;




    private List<filter_FilterDescription> filter_filterdescriptions;




    private List<ContainerMapping> containermappings;




    private List<NodeMapping> nodemappings;




    private List<ContainerMapping> containermappings;




    private Layer layer;




    private tool_ToolSection tool_toolsection;




    private concern_ConcernSet concern_concernset;




    private List<DiagramElementMapping> diagramelementmappings;




    private List<NodeMapping> nodemappings;


    public diagram_description_DiagramDescription(
        String rootExpression,        String preconditionExpression,        boolean enablePopupBars,        String domainClass    ) {
        super(
        );
        this.rootExpression = rootExpression;
        this.preconditionExpression = preconditionExpression;
        this.enablePopupBars = enablePopupBars;
        this.domainClass = domainClass;
        this.layers = new ArrayList<>();
        this.filter_filterdescriptions = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
    }

    public diagram_description_DiagramDescription(
        String rootExpression,        String preconditionExpression,        boolean enablePopupBars,        String domainClass        ArrayList<Layer> layers,        ArrayList<filter_FilterDescription> filter_filterdescriptions,        ArrayList<ContainerMapping> containermappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<ContainerMapping> containermappings,        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<NodeMapping> nodemappings    ) {
        this.rootExpression = rootExpression;
        this.preconditionExpression = preconditionExpression;
        this.enablePopupBars = enablePopupBars;
        this.domainClass = domainClass;
        this.layers = layers;
        this.filter_filterdescriptions = filter_filterdescriptions;
        this.containermappings = containermappings;
        this.nodemappings = nodemappings;
        this.containermappings = containermappings;
        this.diagramelementmappings = diagramelementmappings;
        this.nodemappings = nodemappings;
    }

    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
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
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }

    public List<Layer> getLayers() {
        return layers;
    }

    public void addLayer(Layer layer) {
        this.layers.add(layer);
    }
    public concern_ConcernDescription getConcern_concerndescription() {
        return concern_concerndescription;
    }

    public void setConcern_concerndescription(concern_ConcernDescription concern_concerndescription) {
        this.concern_concerndescription = concern_concerndescription;
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
    public Layer getLayer() {
        return layer;
    }

    public void setLayer(Layer layer) {
        this.layer = layer;
    }
    public tool_ToolSection getTool_toolsection() {
        return tool_toolsection;
    }

    public void setTool_toolsection(tool_ToolSection tool_toolsection) {
        this.tool_toolsection = tool_toolsection;
    }
    public concern_ConcernSet getConcern_concernset() {
        return concern_concernset;
    }

    public void setConcern_concernset(concern_ConcernSet concern_concernset) {
        this.concern_concernset = concern_concernset;
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

}
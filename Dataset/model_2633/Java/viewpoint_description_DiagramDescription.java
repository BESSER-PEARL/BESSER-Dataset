





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DiagramDescription extends description_PasteTargetDescription, description_DragAndDropTargetDescription, description_RepresentationDescription {

    private String rootExpression;
    private boolean enablePopupBars;
    private String domainClass;
    private String preconditionExpression;





    private List<tool_AbstractToolDescription> tool_abstracttooldescriptions;




    private List<description_DiagramElementMapping> description_diagramelementmappings;




    private List<tool_AbstractToolDescription> tool_abstracttooldescriptions;




    private List<filter_FilterDescription> filter_filterdescriptions;




    private concern_ConcernDescription concern_concerndescription;




    private tool_InitialOperation tool_initialoperation;




    private List<description_ContainerMapping> description_containermappings;




    private List<description_NodeMapping> description_nodemappings;




    private List<description_NodeMapping> description_nodemappings;




    private tool_RepresentationCreationDescription tool_representationcreationdescription;




    private List<description_Layer> description_layers;




    private List<tool_AbstractToolDescription> tool_abstracttooldescriptions;




    private validation_ValidationSet validation_validationset;




    private description_Layer description_layer;




    private List<description_ContainerMapping> description_containermappings;


    public viewpoint_description_DiagramDescription(
        String rootExpression,        boolean enablePopupBars,        String domainClass,        String preconditionExpression    ) {
        super(
        );
        this.rootExpression = rootExpression;
        this.enablePopupBars = enablePopupBars;
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.tool_abstracttooldescriptions = new ArrayList<>();
        this.description_diagramelementmappings = new ArrayList<>();
        this.tool_abstracttooldescriptions = new ArrayList<>();
        this.filter_filterdescriptions = new ArrayList<>();
        this.description_containermappings = new ArrayList<>();
        this.description_nodemappings = new ArrayList<>();
        this.description_nodemappings = new ArrayList<>();
        this.description_layers = new ArrayList<>();
        this.tool_abstracttooldescriptions = new ArrayList<>();
        this.description_containermappings = new ArrayList<>();
    }

    public viewpoint_description_DiagramDescription(
        String rootExpression,        boolean enablePopupBars,        String domainClass,        String preconditionExpression        ArrayList<tool_AbstractToolDescription> tool_abstracttooldescriptions,        ArrayList<description_DiagramElementMapping> description_diagramelementmappings,        ArrayList<tool_AbstractToolDescription> tool_abstracttooldescriptions,        ArrayList<filter_FilterDescription> filter_filterdescriptions,        ArrayList<description_ContainerMapping> description_containermappings,        ArrayList<description_NodeMapping> description_nodemappings,        ArrayList<description_NodeMapping> description_nodemappings,        ArrayList<description_Layer> description_layers,        ArrayList<tool_AbstractToolDescription> tool_abstracttooldescriptions,        ArrayList<description_ContainerMapping> description_containermappings    ) {
        this.rootExpression = rootExpression;
        this.enablePopupBars = enablePopupBars;
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.tool_abstracttooldescriptions = tool_abstracttooldescriptions;
        this.description_diagramelementmappings = description_diagramelementmappings;
        this.tool_abstracttooldescriptions = tool_abstracttooldescriptions;
        this.filter_filterdescriptions = filter_filterdescriptions;
        this.description_containermappings = description_containermappings;
        this.description_nodemappings = description_nodemappings;
        this.description_nodemappings = description_nodemappings;
        this.description_layers = description_layers;
        this.tool_abstracttooldescriptions = tool_abstracttooldescriptions;
        this.description_containermappings = description_containermappings;
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
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }

    public List<tool_AbstractToolDescription> getTool_abstracttooldescriptions() {
        return tool_abstracttooldescriptions;
    }

    public void addTool_abstracttooldescription(Tool_abstracttooldescription tool_abstracttooldescription) {
        this.tool_abstracttooldescriptions.add(tool_abstracttooldescription);
    }
    public List<description_DiagramElementMapping> getDescription_diagramelementmappings() {
        return description_diagramelementmappings;
    }

    public void addDescription_diagramelementmapping(Description_diagramelementmapping description_diagramelementmapping) {
        this.description_diagramelementmappings.add(description_diagramelementmapping);
    }
    public List<tool_AbstractToolDescription> getTool_abstracttooldescriptions() {
        return tool_abstracttooldescriptions;
    }

    public void addTool_abstracttooldescription(Tool_abstracttooldescription tool_abstracttooldescription) {
        this.tool_abstracttooldescriptions.add(tool_abstracttooldescription);
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
    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }
    public List<description_ContainerMapping> getDescription_containermappings() {
        return description_containermappings;
    }

    public void addDescription_containermapping(Description_containermapping description_containermapping) {
        this.description_containermappings.add(description_containermapping);
    }
    public List<description_NodeMapping> getDescription_nodemappings() {
        return description_nodemappings;
    }

    public void addDescription_nodemapping(Description_nodemapping description_nodemapping) {
        this.description_nodemappings.add(description_nodemapping);
    }
    public List<description_NodeMapping> getDescription_nodemappings() {
        return description_nodemappings;
    }

    public void addDescription_nodemapping(Description_nodemapping description_nodemapping) {
        this.description_nodemappings.add(description_nodemapping);
    }
    public tool_RepresentationCreationDescription getTool_representationcreationdescription() {
        return tool_representationcreationdescription;
    }

    public void setTool_representationcreationdescription(tool_RepresentationCreationDescription tool_representationcreationdescription) {
        this.tool_representationcreationdescription = tool_representationcreationdescription;
    }
    public List<description_Layer> getDescription_layers() {
        return description_layers;
    }

    public void addDescription_layer(Description_layer description_layer) {
        this.description_layers.add(description_layer);
    }
    public List<tool_AbstractToolDescription> getTool_abstracttooldescriptions() {
        return tool_abstracttooldescriptions;
    }

    public void addTool_abstracttooldescription(Tool_abstracttooldescription tool_abstracttooldescription) {
        this.tool_abstracttooldescriptions.add(tool_abstracttooldescription);
    }
    public validation_ValidationSet getValidation_validationset() {
        return validation_validationset;
    }

    public void setValidation_validationset(validation_ValidationSet validation_validationset) {
        this.validation_validationset = validation_validationset;
    }
    public description_Layer getDescription_layer() {
        return description_layer;
    }

    public void setDescription_layer(description_Layer description_layer) {
        this.description_layer = description_layer;
    }
    public List<description_ContainerMapping> getDescription_containermappings() {
        return description_containermappings;
    }

    public void addDescription_containermapping(Description_containermapping description_containermapping) {
        this.description_containermappings.add(description_containermapping);
    }

}






import java.util.List;
import java.util.ArrayList;

public class component_Component extends IPropertyMap, WrapperObject {

    private String finalize;
    private String typeNameL;
    private String categoryL;
    private String startUp;
    private String componentId;
    private String descriptionL;
    private String shutDown;
    private String venderL;
    private boolean required;
    private String activation;
    private String pathId;
    private String deActivation;
    private String versionL;
    private String initialize;
    private String instanceNameL;
    private String resetting;
    private String compositeTypeL;
    private String outportDirection;





    private component_ExecutionContext component_executioncontext;




    private component_Component component_component;




    private component_ExecutionContext component_executioncontext;




    private component_ExecutionContext component_executioncontext;




    private component_SystemDiagram component_systemdiagram;




    private component_SystemDiagram component_systemdiagram;




    private component_SystemDiagram component_systemdiagram;




    private List<component_ExecutionContext> component_executioncontexts;




    private List<component_ExecutionContext> component_executioncontexts;


    public component_Component(
        String finalize,        String typeNameL,        String categoryL,        String startUp,        String componentId,        String descriptionL,        String shutDown,        String venderL,        boolean required,        String activation,        String pathId,        String deActivation,        String versionL,        String initialize,        String instanceNameL,        String resetting,        String compositeTypeL,        String outportDirection    ) {
        super(
        );
        this.finalize = finalize;
        this.typeNameL = typeNameL;
        this.categoryL = categoryL;
        this.startUp = startUp;
        this.componentId = componentId;
        this.descriptionL = descriptionL;
        this.shutDown = shutDown;
        this.venderL = venderL;
        this.required = required;
        this.activation = activation;
        this.pathId = pathId;
        this.deActivation = deActivation;
        this.versionL = versionL;
        this.initialize = initialize;
        this.instanceNameL = instanceNameL;
        this.resetting = resetting;
        this.compositeTypeL = compositeTypeL;
        this.outportDirection = outportDirection;
        this.component_executioncontexts = new ArrayList<>();
        this.component_executioncontexts = new ArrayList<>();
    }

    public component_Component(
        String finalize,        String typeNameL,        String categoryL,        String startUp,        String componentId,        String descriptionL,        String shutDown,        String venderL,        boolean required,        String activation,        String pathId,        String deActivation,        String versionL,        String initialize,        String instanceNameL,        String resetting,        String compositeTypeL,        String outportDirection        ArrayList<component_ExecutionContext> component_executioncontexts,        ArrayList<component_ExecutionContext> component_executioncontexts    ) {
        this.finalize = finalize;
        this.typeNameL = typeNameL;
        this.categoryL = categoryL;
        this.startUp = startUp;
        this.componentId = componentId;
        this.descriptionL = descriptionL;
        this.shutDown = shutDown;
        this.venderL = venderL;
        this.required = required;
        this.activation = activation;
        this.pathId = pathId;
        this.deActivation = deActivation;
        this.versionL = versionL;
        this.initialize = initialize;
        this.instanceNameL = instanceNameL;
        this.resetting = resetting;
        this.compositeTypeL = compositeTypeL;
        this.outportDirection = outportDirection;
        this.component_executioncontexts = component_executioncontexts;
        this.component_executioncontexts = component_executioncontexts;
    }

    public String getFinalize() {
        return finalize;
    }

    public void setFinalize(String finalize) {
        this.finalize = finalize;
    }
    public String getTypenamel() {
        return typeNameL;
    }

    public void setTypenamel(String typeNameL) {
        this.typeNameL = typeNameL;
    }
    public String getCategoryl() {
        return categoryL;
    }

    public void setCategoryl(String categoryL) {
        this.categoryL = categoryL;
    }
    public String getStartup() {
        return startUp;
    }

    public void setStartup(String startUp) {
        this.startUp = startUp;
    }
    public String getComponentid() {
        return componentId;
    }

    public void setComponentid(String componentId) {
        this.componentId = componentId;
    }
    public String getDescriptionl() {
        return descriptionL;
    }

    public void setDescriptionl(String descriptionL) {
        this.descriptionL = descriptionL;
    }
    public String getShutdown() {
        return shutDown;
    }

    public void setShutdown(String shutDown) {
        this.shutDown = shutDown;
    }
    public String getVenderl() {
        return venderL;
    }

    public void setVenderl(String venderL) {
        this.venderL = venderL;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getActivation() {
        return activation;
    }

    public void setActivation(String activation) {
        this.activation = activation;
    }
    public String getPathid() {
        return pathId;
    }

    public void setPathid(String pathId) {
        this.pathId = pathId;
    }
    public String getDeactivation() {
        return deActivation;
    }

    public void setDeactivation(String deActivation) {
        this.deActivation = deActivation;
    }
    public String getVersionl() {
        return versionL;
    }

    public void setVersionl(String versionL) {
        this.versionL = versionL;
    }
    public String getInitialize() {
        return initialize;
    }

    public void setInitialize(String initialize) {
        this.initialize = initialize;
    }
    public String getInstancenamel() {
        return instanceNameL;
    }

    public void setInstancenamel(String instanceNameL) {
        this.instanceNameL = instanceNameL;
    }
    public String getResetting() {
        return resetting;
    }

    public void setResetting(String resetting) {
        this.resetting = resetting;
    }
    public String getCompositetypel() {
        return compositeTypeL;
    }

    public void setCompositetypel(String compositeTypeL) {
        this.compositeTypeL = compositeTypeL;
    }
    public String getOutportdirection() {
        return outportDirection;
    }

    public void setOutportdirection(String outportDirection) {
        this.outportDirection = outportDirection;
    }

    public component_ExecutionContext getComponent_executioncontext() {
        return component_executioncontext;
    }

    public void setComponent_executioncontext(component_ExecutionContext component_executioncontext) {
        this.component_executioncontext = component_executioncontext;
    }
    public component_Component getComponent_component() {
        return component_component;
    }

    public void setComponent_component(component_Component component_component) {
        this.component_component = component_component;
    }
    public component_ExecutionContext getComponent_executioncontext() {
        return component_executioncontext;
    }

    public void setComponent_executioncontext(component_ExecutionContext component_executioncontext) {
        this.component_executioncontext = component_executioncontext;
    }
    public component_ExecutionContext getComponent_executioncontext() {
        return component_executioncontext;
    }

    public void setComponent_executioncontext(component_ExecutionContext component_executioncontext) {
        this.component_executioncontext = component_executioncontext;
    }
    public component_SystemDiagram getComponent_systemdiagram() {
        return component_systemdiagram;
    }

    public void setComponent_systemdiagram(component_SystemDiagram component_systemdiagram) {
        this.component_systemdiagram = component_systemdiagram;
    }
    public component_SystemDiagram getComponent_systemdiagram() {
        return component_systemdiagram;
    }

    public void setComponent_systemdiagram(component_SystemDiagram component_systemdiagram) {
        this.component_systemdiagram = component_systemdiagram;
    }
    public component_SystemDiagram getComponent_systemdiagram() {
        return component_systemdiagram;
    }

    public void setComponent_systemdiagram(component_SystemDiagram component_systemdiagram) {
        this.component_systemdiagram = component_systemdiagram;
    }
    public List<component_ExecutionContext> getComponent_executioncontexts() {
        return component_executioncontexts;
    }

    public void addComponent_executioncontext(Component_executioncontext component_executioncontext) {
        this.component_executioncontexts.add(component_executioncontext);
    }
    public List<component_ExecutionContext> getComponent_executioncontexts() {
        return component_executioncontexts;
    }

    public void addComponent_executioncontext(Component_executioncontext component_executioncontext) {
        this.component_executioncontexts.add(component_executioncontext);
    }

}






import java.util.List;
import java.util.ArrayList;

public class component_Component extends WrapperObject, IPropertyMap {

    private String descriptionL;
    private String resetting;
    private String pathId;
    private String versionL;
    private String instanceNameL;
    private String categoryL;
    private String initialize;
    private boolean required;
    private String compositeTypeL;
    private String shutDown;
    private String venderL;
    private String finalize;
    private String activation;
    private String deActivation;
    private String typeNameL;
    private String componentId;
    private String outportDirection;
    private String startUp;





    private component_SystemDiagram component_systemdiagram;




    private List<component_ExecutionContext> component_executioncontexts;




    private component_Component component_component;




    private component_SystemDiagram component_systemdiagram;




    private component_SystemDiagram component_systemdiagram;




    private component_ExecutionContext component_executioncontext;




    private component_ExecutionContext component_executioncontext;




    private component_ExecutionContext component_executioncontext;




    private List<component_ExecutionContext> component_executioncontexts;


    public component_Component(
        String descriptionL,        String resetting,        String pathId,        String versionL,        String instanceNameL,        String categoryL,        String initialize,        boolean required,        String compositeTypeL,        String shutDown,        String venderL,        String finalize,        String activation,        String deActivation,        String typeNameL,        String componentId,        String outportDirection,        String startUp    ) {
        super(
        );
        this.descriptionL = descriptionL;
        this.resetting = resetting;
        this.pathId = pathId;
        this.versionL = versionL;
        this.instanceNameL = instanceNameL;
        this.categoryL = categoryL;
        this.initialize = initialize;
        this.required = required;
        this.compositeTypeL = compositeTypeL;
        this.shutDown = shutDown;
        this.venderL = venderL;
        this.finalize = finalize;
        this.activation = activation;
        this.deActivation = deActivation;
        this.typeNameL = typeNameL;
        this.componentId = componentId;
        this.outportDirection = outportDirection;
        this.startUp = startUp;
        this.component_executioncontexts = new ArrayList<>();
        this.component_executioncontexts = new ArrayList<>();
    }

    public component_Component(
        String descriptionL,        String resetting,        String pathId,        String versionL,        String instanceNameL,        String categoryL,        String initialize,        boolean required,        String compositeTypeL,        String shutDown,        String venderL,        String finalize,        String activation,        String deActivation,        String typeNameL,        String componentId,        String outportDirection,        String startUp        ArrayList<component_ExecutionContext> component_executioncontexts,        ArrayList<component_ExecutionContext> component_executioncontexts    ) {
        this.descriptionL = descriptionL;
        this.resetting = resetting;
        this.pathId = pathId;
        this.versionL = versionL;
        this.instanceNameL = instanceNameL;
        this.categoryL = categoryL;
        this.initialize = initialize;
        this.required = required;
        this.compositeTypeL = compositeTypeL;
        this.shutDown = shutDown;
        this.venderL = venderL;
        this.finalize = finalize;
        this.activation = activation;
        this.deActivation = deActivation;
        this.typeNameL = typeNameL;
        this.componentId = componentId;
        this.outportDirection = outportDirection;
        this.startUp = startUp;
        this.component_executioncontexts = component_executioncontexts;
        this.component_executioncontexts = component_executioncontexts;
    }

    public String getDescriptionl() {
        return descriptionL;
    }

    public void setDescriptionl(String descriptionL) {
        this.descriptionL = descriptionL;
    }
    public String getResetting() {
        return resetting;
    }

    public void setResetting(String resetting) {
        this.resetting = resetting;
    }
    public String getPathid() {
        return pathId;
    }

    public void setPathid(String pathId) {
        this.pathId = pathId;
    }
    public String getVersionl() {
        return versionL;
    }

    public void setVersionl(String versionL) {
        this.versionL = versionL;
    }
    public String getInstancenamel() {
        return instanceNameL;
    }

    public void setInstancenamel(String instanceNameL) {
        this.instanceNameL = instanceNameL;
    }
    public String getCategoryl() {
        return categoryL;
    }

    public void setCategoryl(String categoryL) {
        this.categoryL = categoryL;
    }
    public String getInitialize() {
        return initialize;
    }

    public void setInitialize(String initialize) {
        this.initialize = initialize;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getCompositetypel() {
        return compositeTypeL;
    }

    public void setCompositetypel(String compositeTypeL) {
        this.compositeTypeL = compositeTypeL;
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
    public String getFinalize() {
        return finalize;
    }

    public void setFinalize(String finalize) {
        this.finalize = finalize;
    }
    public String getActivation() {
        return activation;
    }

    public void setActivation(String activation) {
        this.activation = activation;
    }
    public String getDeactivation() {
        return deActivation;
    }

    public void setDeactivation(String deActivation) {
        this.deActivation = deActivation;
    }
    public String getTypenamel() {
        return typeNameL;
    }

    public void setTypenamel(String typeNameL) {
        this.typeNameL = typeNameL;
    }
    public String getComponentid() {
        return componentId;
    }

    public void setComponentid(String componentId) {
        this.componentId = componentId;
    }
    public String getOutportdirection() {
        return outportDirection;
    }

    public void setOutportdirection(String outportDirection) {
        this.outportDirection = outportDirection;
    }
    public String getStartup() {
        return startUp;
    }

    public void setStartup(String startUp) {
        this.startUp = startUp;
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
    public component_Component getComponent_component() {
        return component_component;
    }

    public void setComponent_component(component_Component component_component) {
        this.component_component = component_component;
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
    public component_ExecutionContext getComponent_executioncontext() {
        return component_executioncontext;
    }

    public void setComponent_executioncontext(component_ExecutionContext component_executioncontext) {
        this.component_executioncontext = component_executioncontext;
    }
    public List<component_ExecutionContext> getComponent_executioncontexts() {
        return component_executioncontexts;
    }

    public void addComponent_executioncontext(Component_executioncontext component_executioncontext) {
        this.component_executioncontexts.add(component_executioncontext);
    }

}
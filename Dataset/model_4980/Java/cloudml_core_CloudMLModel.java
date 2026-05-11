





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_CloudMLModel extends CloudMLElementWithProperties {






    private List<VM> vms;




    private List<VMInstance> vminstances;




    private List<Provider> providers;




    private List<ExternalComponent> externalcomponents;




    private List<InternalComponent> internalcomponents;




    private List<InternalComponentInstance> internalcomponentinstances;




    private List<ExternalComponentInstance> externalcomponentinstances;




    private List<ComponentInstance> componentinstances;




    private List<Cloud> clouds;




    private List<Component> components;


    public cloudml_core_CloudMLModel(
    ) {
        super(
        );
        this.vms = new ArrayList<>();
        this.vminstances = new ArrayList<>();
        this.providers = new ArrayList<>();
        this.externalcomponents = new ArrayList<>();
        this.internalcomponents = new ArrayList<>();
        this.internalcomponentinstances = new ArrayList<>();
        this.externalcomponentinstances = new ArrayList<>();
        this.componentinstances = new ArrayList<>();
        this.clouds = new ArrayList<>();
        this.components = new ArrayList<>();
    }

    public cloudml_core_CloudMLModel(
        ArrayList<VM> vms,        ArrayList<VMInstance> vminstances,        ArrayList<Provider> providers,        ArrayList<ExternalComponent> externalcomponents,        ArrayList<InternalComponent> internalcomponents,        ArrayList<InternalComponentInstance> internalcomponentinstances,        ArrayList<ExternalComponentInstance> externalcomponentinstances,        ArrayList<ComponentInstance> componentinstances,        ArrayList<Cloud> clouds,        ArrayList<Component> components    ) {
        this.vms = vms;
        this.vminstances = vminstances;
        this.providers = providers;
        this.externalcomponents = externalcomponents;
        this.internalcomponents = internalcomponents;
        this.internalcomponentinstances = internalcomponentinstances;
        this.externalcomponentinstances = externalcomponentinstances;
        this.componentinstances = componentinstances;
        this.clouds = clouds;
        this.components = components;
    }


    public List<VM> getVms() {
        return vms;
    }

    public void addVm(Vm vm) {
        this.vms.add(vm);
    }
    public List<VMInstance> getVminstances() {
        return vminstances;
    }

    public void addVminstance(Vminstance vminstance) {
        this.vminstances.add(vminstance);
    }
    public List<Provider> getProviders() {
        return providers;
    }

    public void addProvider(Provider provider) {
        this.providers.add(provider);
    }
    public List<ExternalComponent> getExternalcomponents() {
        return externalcomponents;
    }

    public void addExternalcomponent(Externalcomponent externalcomponent) {
        this.externalcomponents.add(externalcomponent);
    }
    public List<InternalComponent> getInternalcomponents() {
        return internalcomponents;
    }

    public void addInternalcomponent(Internalcomponent internalcomponent) {
        this.internalcomponents.add(internalcomponent);
    }
    public List<InternalComponentInstance> getInternalcomponentinstances() {
        return internalcomponentinstances;
    }

    public void addInternalcomponentinstance(Internalcomponentinstance internalcomponentinstance) {
        this.internalcomponentinstances.add(internalcomponentinstance);
    }
    public List<ExternalComponentInstance> getExternalcomponentinstances() {
        return externalcomponentinstances;
    }

    public void addExternalcomponentinstance(Externalcomponentinstance externalcomponentinstance) {
        this.externalcomponentinstances.add(externalcomponentinstance);
    }
    public List<ComponentInstance> getComponentinstances() {
        return componentinstances;
    }

    public void addComponentinstance(Componentinstance componentinstance) {
        this.componentinstances.add(componentinstance);
    }
    public List<Cloud> getClouds() {
        return clouds;
    }

    public void addCloud(Cloud cloud) {
        this.clouds.add(cloud);
    }
    public List<Component> getComponents() {
        return components;
    }

    public void addComponent(Component component) {
        this.components.add(component);
    }

}
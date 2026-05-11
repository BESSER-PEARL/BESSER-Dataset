





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_Link  {

    private String name;





    private List<componentBasedSystem_Container> componentbasedsystem_containers;




    private componentBasedSystem_Environment componentbasedsystem_environment;


    public componentBasedSystem_Link(
        String name    ) {
        this.name = name;
        this.componentbasedsystem_containers = new ArrayList<>();
    }

    public componentBasedSystem_Link(
        String name        ArrayList<componentBasedSystem_Container> componentbasedsystem_containers    ) {
        this.name = name;
        this.componentbasedsystem_containers = componentbasedsystem_containers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<componentBasedSystem_Container> getComponentbasedsystem_containers() {
        return componentbasedsystem_containers;
    }

    public void addComponentbasedsystem_container(Componentbasedsystem_container componentbasedsystem_container) {
        this.componentbasedsystem_containers.add(componentbasedsystem_container);
    }
    public componentBasedSystem_Environment getComponentbasedsystem_environment() {
        return componentbasedsystem_environment;
    }

    public void setComponentbasedsystem_environment(componentBasedSystem_Environment componentbasedsystem_environment) {
        this.componentbasedsystem_environment = componentbasedsystem_environment;
    }

}
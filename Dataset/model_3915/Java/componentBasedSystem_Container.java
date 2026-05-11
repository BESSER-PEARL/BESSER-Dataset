





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_Container  {

    private String name;





    private componentBasedSystem_Environment componentbasedsystem_environment;


    public componentBasedSystem_Container(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentBasedSystem_Environment getComponentbasedsystem_environment() {
        return componentbasedsystem_environment;
    }

    public void setComponentbasedsystem_environment(componentBasedSystem_Environment componentbasedsystem_environment) {
        this.componentbasedsystem_environment = componentbasedsystem_environment;
    }

}
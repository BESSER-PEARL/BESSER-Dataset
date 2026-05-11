





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_Interface  {

    private String name;





    private componentBasedSystem_Repository componentbasedsystem_repository;


    public componentBasedSystem_Interface(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentBasedSystem_Repository getComponentbasedsystem_repository() {
        return componentbasedsystem_repository;
    }

    public void setComponentbasedsystem_repository(componentBasedSystem_Repository componentbasedsystem_repository) {
        this.componentbasedsystem_repository = componentbasedsystem_repository;
    }

}
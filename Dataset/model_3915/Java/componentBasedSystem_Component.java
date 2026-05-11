





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_Component  {

    private String name;





    private componentBasedSystem_Repository componentbasedsystem_repository;




    private List<ProvidedRole> providedroles;




    private List<RequiredRole> requiredroles;


    public componentBasedSystem_Component(
        String name    ) {
        this.name = name;
        this.providedroles = new ArrayList<>();
        this.requiredroles = new ArrayList<>();
    }

    public componentBasedSystem_Component(
        String name        ArrayList<ProvidedRole> providedroles,        ArrayList<RequiredRole> requiredroles    ) {
        this.name = name;
        this.providedroles = providedroles;
        this.requiredroles = requiredroles;
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
    public List<ProvidedRole> getProvidedroles() {
        return providedroles;
    }

    public void addProvidedrole(Providedrole providedrole) {
        this.providedroles.add(providedrole);
    }
    public List<RequiredRole> getRequiredroles() {
        return requiredroles;
    }

    public void addRequiredrole(Requiredrole requiredrole) {
        this.requiredroles.add(requiredrole);
    }

}
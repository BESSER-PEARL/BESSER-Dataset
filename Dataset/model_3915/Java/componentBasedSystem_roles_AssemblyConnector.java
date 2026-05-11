





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_roles_AssemblyConnector  {

    private String name;





    private RequiredRole requiredrole;




    private ProvidedRole providedrole;


    public componentBasedSystem_roles_AssemblyConnector(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RequiredRole getRequiredrole() {
        return requiredrole;
    }

    public void setRequiredrole(RequiredRole requiredrole) {
        this.requiredrole = requiredrole;
    }
    public ProvidedRole getProvidedrole() {
        return providedrole;
    }

    public void setProvidedrole(ProvidedRole providedrole) {
        this.providedrole = providedrole;
    }

}
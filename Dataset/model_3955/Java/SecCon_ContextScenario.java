





import java.util.List;
import java.util.ArrayList;

public class SecCon_ContextScenario  {

    private String name;





    private SecCon_Project seccon_project;


    public SecCon_ContextScenario(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SecCon_Project getSeccon_project() {
        return seccon_project;
    }

    public void setSeccon_project(SecCon_Project seccon_project) {
        this.seccon_project = seccon_project;
    }

}






import java.util.List;
import java.util.ArrayList;

public class architecture_Component  {

    private String name;





    private architecture_AbstractModel architecture_abstractmodel;


    public architecture_Component(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public architecture_AbstractModel getArchitecture_abstractmodel() {
        return architecture_abstractmodel;
    }

    public void setArchitecture_abstractmodel(architecture_AbstractModel architecture_abstractmodel) {
        this.architecture_abstractmodel = architecture_abstractmodel;
    }

}
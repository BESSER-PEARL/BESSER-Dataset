





import java.util.List;
import java.util.ArrayList;

public class architecture_DomainDeclaration  {

    private String name;





    private architecture_Model architecture_model;


    public architecture_DomainDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public architecture_Model getArchitecture_model() {
        return architecture_model;
    }

    public void setArchitecture_model(architecture_Model architecture_model) {
        this.architecture_model = architecture_model;
    }

}
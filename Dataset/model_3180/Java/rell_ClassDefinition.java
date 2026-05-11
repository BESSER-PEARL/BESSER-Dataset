





import java.util.List;
import java.util.ArrayList;

public class rell_ClassDefinition  {

    private String name;





    private rell_Model rell_model;




    private rell_ClassDefinition rell_classdefinition;


    public rell_ClassDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rell_Model getRell_model() {
        return rell_model;
    }

    public void setRell_model(rell_Model rell_model) {
        this.rell_model = rell_model;
    }
    public rell_ClassDefinition getRell_classdefinition() {
        return rell_classdefinition;
    }

    public void setRell_classdefinition(rell_ClassDefinition rell_classdefinition) {
        this.rell_classdefinition = rell_classdefinition;
    }

}
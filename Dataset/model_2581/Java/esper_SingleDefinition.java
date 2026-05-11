





import java.util.List;
import java.util.ArrayList;

public class esper_SingleDefinition  {

    private String name;





    private esper_SingleSelectDefinition esper_singleselectdefinition;


    public esper_SingleDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public esper_SingleSelectDefinition getEsper_singleselectdefinition() {
        return esper_singleselectdefinition;
    }

    public void setEsper_singleselectdefinition(esper_SingleSelectDefinition esper_singleselectdefinition) {
        this.esper_singleselectdefinition = esper_singleselectdefinition;
    }

}
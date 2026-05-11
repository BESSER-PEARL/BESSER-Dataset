





import java.util.List;
import java.util.ArrayList;

public class dg_Definitions  {






    private List<dg_Definition> dg_definitions;


    public dg_Definitions(
    ) {
        this.dg_definitions = new ArrayList<>();
    }

    public dg_Definitions(
        ArrayList<dg_Definition> dg_definitions    ) {
        this.dg_definitions = dg_definitions;
    }


    public List<dg_Definition> getDg_definitions() {
        return dg_definitions;
    }

    public void addDg_definition(Dg_definition dg_definition) {
        this.dg_definitions.add(dg_definition);
    }

}
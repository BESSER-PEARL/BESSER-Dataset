





import java.util.List;
import java.util.ArrayList;

public class esper_KindOfEvent  {

    private String name;





    private esper_SingleDefinition esper_singledefinition;


    public esper_KindOfEvent(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public esper_SingleDefinition getEsper_singledefinition() {
        return esper_singledefinition;
    }

    public void setEsper_singledefinition(esper_SingleDefinition esper_singledefinition) {
        this.esper_singledefinition = esper_singledefinition;
    }

}
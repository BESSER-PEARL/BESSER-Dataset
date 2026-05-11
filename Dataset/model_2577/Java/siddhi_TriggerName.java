





import java.util.List;
import java.util.ArrayList;

public class siddhi_TriggerName  {

    private String id;





    private siddhi_DefinitionTrigger siddhi_definitiontrigger;


    public siddhi_TriggerName(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public siddhi_DefinitionTrigger getSiddhi_definitiontrigger() {
        return siddhi_definitiontrigger;
    }

    public void setSiddhi_definitiontrigger(siddhi_DefinitionTrigger siddhi_definitiontrigger) {
        this.siddhi_definitiontrigger = siddhi_definitiontrigger;
    }

}
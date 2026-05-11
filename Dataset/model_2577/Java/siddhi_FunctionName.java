





import java.util.List;
import java.util.ArrayList;

public class siddhi_FunctionName  {

    private String id;





    private siddhi_DefinitionFunction siddhi_definitionfunction;


    public siddhi_FunctionName(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public siddhi_DefinitionFunction getSiddhi_definitionfunction() {
        return siddhi_definitionfunction;
    }

    public void setSiddhi_definitionfunction(siddhi_DefinitionFunction siddhi_definitionfunction) {
        this.siddhi_definitionfunction = siddhi_definitionfunction;
    }

}






import java.util.List;
import java.util.ArrayList;

public class siddhi_FunctionBody  {

    private String value;





    private siddhi_DefinitionFunction siddhi_definitionfunction;


    public siddhi_FunctionBody(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public siddhi_DefinitionFunction getSiddhi_definitionfunction() {
        return siddhi_definitionfunction;
    }

    public void setSiddhi_definitionfunction(siddhi_DefinitionFunction siddhi_definitionfunction) {
        this.siddhi_definitionfunction = siddhi_definitionfunction;
    }

}
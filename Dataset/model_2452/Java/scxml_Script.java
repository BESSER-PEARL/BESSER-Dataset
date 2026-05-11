





import java.util.List;
import java.util.ArrayList;

public class scxml_Script  {

    private String value;





    private scxml_StateChart scxml_statechart;


    public scxml_Script(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public scxml_StateChart getScxml_statechart() {
        return scxml_statechart;
    }

    public void setScxml_statechart(scxml_StateChart scxml_statechart) {
        this.scxml_statechart = scxml_statechart;
    }

}
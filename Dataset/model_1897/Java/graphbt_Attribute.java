





import java.util.List;
import java.util.ArrayList;

public class graphbt_Attribute  {

    private String name;
    private String type;
    private String value;





    private graphbt_Component graphbt_component;


    public graphbt_Attribute(
        String name,        String type,        String value    ) {
        this.name = name;
        this.type = type;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }

}






import java.util.List;
import java.util.ArrayList;

public class graphbt_Attribute  {

    private String name;
    private String value;
    private String type;





    private graphbt_Component graphbt_component;


    public graphbt_Attribute(
        String name,        String value,        String type    ) {
        this.name = name;
        this.value = value;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }

}






import java.util.List;
import java.util.ArrayList;

public class esper_AttributesDefinition  {

    private String type;
    private String name;





    private esper_Attributes esper_attributes;


    public esper_AttributesDefinition(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public esper_Attributes getEsper_attributes() {
        return esper_attributes;
    }

    public void setEsper_attributes(esper_Attributes esper_attributes) {
        this.esper_attributes = esper_attributes;
    }

}
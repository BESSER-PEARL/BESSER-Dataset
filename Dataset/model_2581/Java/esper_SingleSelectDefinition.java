





import java.util.List;
import java.util.ArrayList;

public class esper_SingleSelectDefinition  {

    private String attribute;





    private esper_KindSelectAttributesDefinition esper_kindselectattributesdefinition;


    public esper_SingleSelectDefinition(
        String attribute    ) {
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public esper_KindSelectAttributesDefinition getEsper_kindselectattributesdefinition() {
        return esper_kindselectattributesdefinition;
    }

    public void setEsper_kindselectattributesdefinition(esper_KindSelectAttributesDefinition esper_kindselectattributesdefinition) {
        this.esper_kindselectattributesdefinition = esper_kindselectattributesdefinition;
    }

}
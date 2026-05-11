





import java.util.List;
import java.util.ArrayList;

public class esper_DefaultMethods  {

    private String name;





    private esper_Having esper_having;




    private esper_KindSelectAttributesDefinition esper_kindselectattributesdefinition;


    public esper_DefaultMethods(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public esper_Having getEsper_having() {
        return esper_having;
    }

    public void setEsper_having(esper_Having esper_having) {
        this.esper_having = esper_having;
    }
    public esper_KindSelectAttributesDefinition getEsper_kindselectattributesdefinition() {
        return esper_kindselectattributesdefinition;
    }

    public void setEsper_kindselectattributesdefinition(esper_KindSelectAttributesDefinition esper_kindselectattributesdefinition) {
        this.esper_kindselectattributesdefinition = esper_kindselectattributesdefinition;
    }

}
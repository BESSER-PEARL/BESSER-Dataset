





import java.util.List;
import java.util.ArrayList;

public class entity_JAVAID  {

    private String name;





    private entity_TypeDef entity_typedef;


    public entity_JAVAID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entity_TypeDef getEntity_typedef() {
        return entity_typedef;
    }

    public void setEntity_typedef(entity_TypeDef entity_typedef) {
        this.entity_typedef = entity_typedef;
    }

}
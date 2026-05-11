





import java.util.List;
import java.util.ArrayList;

public class entities_JAVAID  {

    private String name;





    private entities_TypeDef entities_typedef;


    public entities_JAVAID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entities_TypeDef getEntities_typedef() {
        return entities_typedef;
    }

    public void setEntities_typedef(entities_TypeDef entities_typedef) {
        this.entities_typedef = entities_typedef;
    }

}
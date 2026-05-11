





import java.util.List;
import java.util.ArrayList;

public class rell_Attribute  {

    private String modificator;





    private rell_ClassDefinition rell_classdefinition;


    public rell_Attribute(
        String modificator    ) {
        this.modificator = modificator;
    }


    public String getModificator() {
        return modificator;
    }

    public void setModificator(String modificator) {
        this.modificator = modificator;
    }

    public rell_ClassDefinition getRell_classdefinition() {
        return rell_classdefinition;
    }

    public void setRell_classdefinition(rell_ClassDefinition rell_classdefinition) {
        this.rell_classdefinition = rell_classdefinition;
    }

}
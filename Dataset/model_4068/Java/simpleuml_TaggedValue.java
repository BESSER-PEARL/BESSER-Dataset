





import java.util.List;
import java.util.ArrayList;

public class simpleuml_TaggedValue  {

    private String name;
    private String value;





    private simpleuml_ModelElement simpleuml_modelelement;


    public simpleuml_TaggedValue(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
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

    public simpleuml_ModelElement getSimpleuml_modelelement() {
        return simpleuml_modelelement;
    }

    public void setSimpleuml_modelelement(simpleuml_ModelElement simpleuml_modelelement) {
        this.simpleuml_modelelement = simpleuml_modelelement;
    }

}
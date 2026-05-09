





import java.util.List;
import java.util.ArrayList;

public class henshin_Annotation extends ModelElement {

    private String key;
    private String value;





    private henshin_ModelElement henshin_modelelement;


    public henshin_Annotation(
        String key,        String value    ) {
        super(
        );
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public henshin_ModelElement getHenshin_modelelement() {
        return henshin_modelelement;
    }

    public void setHenshin_modelelement(henshin_ModelElement henshin_modelelement) {
        this.henshin_modelelement = henshin_modelelement;
    }

}
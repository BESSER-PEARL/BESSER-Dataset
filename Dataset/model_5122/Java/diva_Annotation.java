





import java.util.List;
import java.util.ArrayList;

public class diva_Annotation extends Visitable {

    private String key;
    private String value;





    private diva_DiVAModelElement diva_divamodelelement;


    public diva_Annotation(
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

    public diva_DiVAModelElement getDiva_divamodelelement() {
        return diva_divamodelelement;
    }

    public void setDiva_divamodelelement(diva_DiVAModelElement diva_divamodelelement) {
        this.diva_divamodelelement = diva_divamodelelement;
    }

}
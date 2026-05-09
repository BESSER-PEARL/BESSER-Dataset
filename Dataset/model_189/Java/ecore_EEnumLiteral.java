





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnumLiteral extends ENamedElement {

    private String instance;
    private String literal;
    private int value;





    private ecore_EEnum ecore_eenum;




    private ecore_EEnum ecore_eenum;


    public ecore_EEnumLiteral(
        String instance,        String literal,        int value    ) {
        super(
        );
        this.instance = instance;
        this.literal = literal;
        this.value = value;
    }


    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public ecore_EEnum getEcore_eenum() {
        return ecore_eenum;
    }

    public void setEcore_eenum(ecore_EEnum ecore_eenum) {
        this.ecore_eenum = ecore_eenum;
    }
    public ecore_EEnum getEcore_eenum() {
        return ecore_eenum;
    }

    public void setEcore_eenum(ecore_EEnum ecore_eenum) {
        this.ecore_eenum = ecore_eenum;
    }

}
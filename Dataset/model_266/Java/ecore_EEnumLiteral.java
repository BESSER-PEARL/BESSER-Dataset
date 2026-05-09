





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnumLiteral extends ENamedElement {

    private int value;
    private String instance;



    public ecore_EEnumLiteral(
        int value,        String instance    ) {
        super(
        );
        this.value = value;
        this.instance = instance;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }


}
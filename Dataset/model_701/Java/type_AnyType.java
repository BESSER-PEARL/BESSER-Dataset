





import java.util.List;
import java.util.ArrayList;

public class type_AnyType  {

    private String anyAttribute;
    private String mixed;
    private String any;



    public type_AnyType(
        String anyAttribute,        String mixed,        String any    ) {
        this.anyAttribute = anyAttribute;
        this.mixed = mixed;
        this.any = any;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }


}
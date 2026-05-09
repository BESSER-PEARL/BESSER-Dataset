





import java.util.List;
import java.util.ArrayList;

public class type_AnyType  {

    private String anyAttribute;
    private String any;
    private String mixed;



    public type_AnyType(
        String anyAttribute,        String any,        String mixed    ) {
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.mixed = mixed;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}
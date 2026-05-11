





import java.util.List;
import java.util.ArrayList;

public class xal_PostBoxNumberExtension  {

    private String anyAttribute;
    private String numberExtensionSeparator;
    private String mixed;



    public xal_PostBoxNumberExtension(
        String anyAttribute,        String numberExtensionSeparator,        String mixed    ) {
        this.anyAttribute = anyAttribute;
        this.numberExtensionSeparator = numberExtensionSeparator;
        this.mixed = mixed;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getNumberextensionseparator() {
        return numberExtensionSeparator;
    }

    public void setNumberextensionseparator(String numberExtensionSeparator) {
        this.numberExtensionSeparator = numberExtensionSeparator;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}
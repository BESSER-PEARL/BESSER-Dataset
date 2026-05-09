





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_PinMode  {

    private String name;
    private String value;





    private MicrocontrollerModeling_CLanguage microcontrollermodeling_clanguage;


    public MicrocontrollerModeling_PinMode(
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

    public MicrocontrollerModeling_CLanguage getMicrocontrollermodeling_clanguage() {
        return microcontrollermodeling_clanguage;
    }

    public void setMicrocontrollermodeling_clanguage(MicrocontrollerModeling_CLanguage microcontrollermodeling_clanguage) {
        this.microcontrollermodeling_clanguage = microcontrollermodeling_clanguage;
    }

}






import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_PinOperation extends Function {

    private String name;





    private MicrocontrollerModeling_CLanguage microcontrollermodeling_clanguage;


    public MicrocontrollerModeling_PinOperation(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MicrocontrollerModeling_CLanguage getMicrocontrollermodeling_clanguage() {
        return microcontrollermodeling_clanguage;
    }

    public void setMicrocontrollermodeling_clanguage(MicrocontrollerModeling_CLanguage microcontrollermodeling_clanguage) {
        this.microcontrollermodeling_clanguage = microcontrollermodeling_clanguage;
    }

}
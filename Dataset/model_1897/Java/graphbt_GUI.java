





import java.util.List;
import java.util.ArrayList;

public class graphbt_GUI  {

    private String codeImplementation;
    private String identifier;



    public graphbt_GUI(
        String codeImplementation,        String identifier    ) {
        this.codeImplementation = codeImplementation;
        this.identifier = identifier;
    }


    public String getCodeimplementation() {
        return codeImplementation;
    }

    public void setCodeimplementation(String codeImplementation) {
        this.codeImplementation = codeImplementation;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}
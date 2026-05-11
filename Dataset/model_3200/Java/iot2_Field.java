





import java.util.List;
import java.util.ArrayList;

public class iot2_Field extends Typed {

    private String identifier;





    private iot2_ExceptionDef iot2_exceptiondef;


    public iot2_Field(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public iot2_ExceptionDef getIot2_exceptiondef() {
        return iot2_exceptiondef;
    }

    public void setIot2_exceptiondef(iot2_ExceptionDef iot2_exceptiondef) {
        this.iot2_exceptiondef = iot2_exceptiondef;
    }

}






import java.util.List;
import java.util.ArrayList;

public class iot2_IDLType  {

    private String typeCode;





    private iot2_Typed iot2_typed;


    public iot2_IDLType(
        String typeCode    ) {
        this.typeCode = typeCode;
    }


    public String getTypecode() {
        return typeCode;
    }

    public void setTypecode(String typeCode) {
        this.typeCode = typeCode;
    }

    public iot2_Typed getIot2_typed() {
        return iot2_typed;
    }

    public void setIot2_typed(iot2_Typed iot2_typed) {
        this.iot2_typed = iot2_typed;
    }

}
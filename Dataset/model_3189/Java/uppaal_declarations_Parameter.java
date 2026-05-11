





import java.util.List;
import java.util.ArrayList;

public class uppaal_declarations_Parameter extends Variable {

    private String callType;



    public uppaal_declarations_Parameter(
        String callType    ) {
        super(
        );
        this.callType = callType;
    }


    public String getCalltype() {
        return callType;
    }

    public void setCalltype(String callType) {
        this.callType = callType;
    }


}
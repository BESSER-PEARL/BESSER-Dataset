





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FTA_Gate extends Cause {

    private String gateType;



    public failureLogic_FTA_Gate(
        String gateType    ) {
        super(
        );
        this.gateType = gateType;
    }


    public String getGatetype() {
        return gateType;
    }

    public void setGatetype(String gateType) {
        this.gateType = gateType;
    }


}
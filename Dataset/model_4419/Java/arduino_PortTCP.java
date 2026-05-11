





import java.util.List;
import java.util.ArrayList;

public class arduino_PortTCP extends PortProtocol {

    private String supportType;



    public arduino_PortTCP(
        String supportType    ) {
        super(
        );
        this.supportType = supportType;
    }


    public String getSupporttype() {
        return supportType;
    }

    public void setSupporttype(String supportType) {
        this.supportType = supportType;
    }


}
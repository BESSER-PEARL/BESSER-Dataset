





import java.util.List;
import java.util.ArrayList;

public class iot_Branching extends Controller {






    private iot_IfPort iot_ifport;




    private iot_ThenPort iot_thenport;




    private iot_ElsePort iot_elseport;


    public iot_Branching(
    ) {
        super(
        );
    }



    public iot_IfPort getIot_ifport() {
        return iot_ifport;
    }

    public void setIot_ifport(iot_IfPort iot_ifport) {
        this.iot_ifport = iot_ifport;
    }
    public iot_ThenPort getIot_thenport() {
        return iot_thenport;
    }

    public void setIot_thenport(iot_ThenPort iot_thenport) {
        this.iot_thenport = iot_thenport;
    }
    public iot_ElsePort getIot_elseport() {
        return iot_elseport;
    }

    public void setIot_elseport(iot_ElsePort iot_elseport) {
        this.iot_elseport = iot_elseport;
    }

}
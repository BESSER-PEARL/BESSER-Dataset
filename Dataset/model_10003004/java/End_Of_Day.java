





import java.util.List;
import java.util.ArrayList;

public class End_Of_Day  {

    private int EOT;





    private Gateway gateway;


    public End_Of_Day(
        int EOT    ) {
        this.EOT = EOT;
    }


    public int getEot() {
        return EOT;
    }

    public void setEot(int EOT) {
        this.EOT = EOT;
    }

    public Gateway getGateway() {
        return gateway;
    }

    public void setGateway(Gateway gateway) {
        this.gateway = gateway;
    }

}
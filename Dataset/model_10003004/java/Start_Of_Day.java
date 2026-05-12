





import java.util.List;
import java.util.ArrayList;

public class Start_Of_Day  {

    private int SOT;





    private Gateway gateway;


    public Start_Of_Day(
        int SOT    ) {
        this.SOT = SOT;
    }


    public int getSot() {
        return SOT;
    }

    public void setSot(int SOT) {
        this.SOT = SOT;
    }

    public Gateway getGateway() {
        return gateway;
    }

    public void setGateway(Gateway gateway) {
        this.gateway = gateway;
    }

}
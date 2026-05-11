





import java.util.List;
import java.util.ArrayList;

public class wsn_Data  {






    private wsn_Comm wsn_comm;




    private wsn_IData wsn_idata;




    private wsn_Actuating wsn_actuating;




    private wsn_Sensing wsn_sensing;




    private wsn_Message wsn_message;


    public wsn_Data(
    ) {
    }



    public wsn_Comm getWsn_comm() {
        return wsn_comm;
    }

    public void setWsn_comm(wsn_Comm wsn_comm) {
        this.wsn_comm = wsn_comm;
    }
    public wsn_IData getWsn_idata() {
        return wsn_idata;
    }

    public void setWsn_idata(wsn_IData wsn_idata) {
        this.wsn_idata = wsn_idata;
    }
    public wsn_Actuating getWsn_actuating() {
        return wsn_actuating;
    }

    public void setWsn_actuating(wsn_Actuating wsn_actuating) {
        this.wsn_actuating = wsn_actuating;
    }
    public wsn_Sensing getWsn_sensing() {
        return wsn_sensing;
    }

    public void setWsn_sensing(wsn_Sensing wsn_sensing) {
        this.wsn_sensing = wsn_sensing;
    }
    public wsn_Message getWsn_message() {
        return wsn_message;
    }

    public void setWsn_message(wsn_Message wsn_message) {
        this.wsn_message = wsn_message;
    }

}
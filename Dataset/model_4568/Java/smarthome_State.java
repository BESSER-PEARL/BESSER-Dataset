





import java.util.List;
import java.util.ArrayList;

public class smarthome_State  {

    private String state;





    private smarthome_FilterConnection smarthome_filterconnection;




    private smarthome_Item smarthome_item;


    public smarthome_State(
        String state    ) {
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public smarthome_FilterConnection getSmarthome_filterconnection() {
        return smarthome_filterconnection;
    }

    public void setSmarthome_filterconnection(smarthome_FilterConnection smarthome_filterconnection) {
        this.smarthome_filterconnection = smarthome_filterconnection;
    }
    public smarthome_Item getSmarthome_item() {
        return smarthome_item;
    }

    public void setSmarthome_item(smarthome_Item smarthome_item) {
        this.smarthome_item = smarthome_item;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ioT_Portnumber  {

    private int number;





    private ioT_Server iot_server;


    public ioT_Portnumber(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public ioT_Server getIot_server() {
        return iot_server;
    }

    public void setIot_server(ioT_Server iot_server) {
        this.iot_server = iot_server;
    }

}
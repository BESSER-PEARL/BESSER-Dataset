





import java.util.List;
import java.util.ArrayList;

public class pycom_Connection  {

    private String portnumber;





    private pycom_Server pycom_server;


    public pycom_Connection(
        String portnumber    ) {
        this.portnumber = portnumber;
    }


    public String getPortnumber() {
        return portnumber;
    }

    public void setPortnumber(String portnumber) {
        this.portnumber = portnumber;
    }

    public pycom_Server getPycom_server() {
        return pycom_server;
    }

    public void setPycom_server(pycom_Server pycom_server) {
        this.pycom_server = pycom_server;
    }

}
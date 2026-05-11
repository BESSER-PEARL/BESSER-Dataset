





import java.util.List;
import java.util.ArrayList;

public class pycom_Host  {

    private String ipAdr;
    private String website;





    private pycom_Connection pycom_connection;


    public pycom_Host(
        String ipAdr,        String website    ) {
        this.ipAdr = ipAdr;
        this.website = website;
    }


    public String getIpadr() {
        return ipAdr;
    }

    public void setIpadr(String ipAdr) {
        this.ipAdr = ipAdr;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }

    public pycom_Connection getPycom_connection() {
        return pycom_connection;
    }

    public void setPycom_connection(pycom_Connection pycom_connection) {
        this.pycom_connection = pycom_connection;
    }

}
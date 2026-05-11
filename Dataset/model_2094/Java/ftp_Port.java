





import java.util.List;
import java.util.ArrayList;

public class ftp_Port  {

    private String name;
    private String type;





    private ftp_PortValue ftp_portvalue;




    private ftp_Connection ftp_connection;




    private ftp_Connection ftp_connection;


    public ftp_Port(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ftp_PortValue getFtp_portvalue() {
        return ftp_portvalue;
    }

    public void setFtp_portvalue(ftp_PortValue ftp_portvalue) {
        this.ftp_portvalue = ftp_portvalue;
    }
    public ftp_Connection getFtp_connection() {
        return ftp_connection;
    }

    public void setFtp_connection(ftp_Connection ftp_connection) {
        this.ftp_connection = ftp_connection;
    }
    public ftp_Connection getFtp_connection() {
        return ftp_connection;
    }

    public void setFtp_connection(ftp_Connection ftp_connection) {
        this.ftp_connection = ftp_connection;
    }

}
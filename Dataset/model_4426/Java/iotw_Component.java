





import java.util.List;
import java.util.ArrayList;

public class iotw_Component  {

    private String id;
    private String constraints;





    private iotw_Connection iotw_connection;




    private iotw_Connection iotw_connection;


    public iotw_Component(
        String id,        String constraints    ) {
        this.id = id;
        this.constraints = constraints;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getConstraints() {
        return constraints;
    }

    public void setConstraints(String constraints) {
        this.constraints = constraints;
    }

    public iotw_Connection getIotw_connection() {
        return iotw_connection;
    }

    public void setIotw_connection(iotw_Connection iotw_connection) {
        this.iotw_connection = iotw_connection;
    }
    public iotw_Connection getIotw_connection() {
        return iotw_connection;
    }

    public void setIotw_connection(iotw_Connection iotw_connection) {
        this.iotw_connection = iotw_connection;
    }

}
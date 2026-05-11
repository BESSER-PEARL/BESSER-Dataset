





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_WebService  {






    private wsmodel3_WebServer wsmodel3_webserver;




    private wsmodel3_DBServer wsmodel3_dbserver;




    private wsmodel3_System wsmodel3_system;




    private List<wsmodel3_REST> wsmodel3_rests;


    public wsmodel3_WebService(
    ) {
        this.wsmodel3_rests = new ArrayList<>();
    }

    public wsmodel3_WebService(
        ArrayList<wsmodel3_REST> wsmodel3_rests    ) {
        this.wsmodel3_rests = wsmodel3_rests;
    }


    public wsmodel3_WebServer getWsmodel3_webserver() {
        return wsmodel3_webserver;
    }

    public void setWsmodel3_webserver(wsmodel3_WebServer wsmodel3_webserver) {
        this.wsmodel3_webserver = wsmodel3_webserver;
    }
    public wsmodel3_DBServer getWsmodel3_dbserver() {
        return wsmodel3_dbserver;
    }

    public void setWsmodel3_dbserver(wsmodel3_DBServer wsmodel3_dbserver) {
        this.wsmodel3_dbserver = wsmodel3_dbserver;
    }
    public wsmodel3_System getWsmodel3_system() {
        return wsmodel3_system;
    }

    public void setWsmodel3_system(wsmodel3_System wsmodel3_system) {
        this.wsmodel3_system = wsmodel3_system;
    }
    public List<wsmodel3_REST> getWsmodel3_rests() {
        return wsmodel3_rests;
    }

    public void addWsmodel3_rest(Wsmodel3_rest wsmodel3_rest) {
        this.wsmodel3_rests.add(wsmodel3_rest);
    }

}
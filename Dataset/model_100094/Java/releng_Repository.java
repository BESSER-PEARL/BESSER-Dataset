





import java.util.List;
import java.util.ArrayList;

public class releng_Repository  {

    private String location;





    private releng_BuildJob releng_buildjob;




    private releng_Server releng_server;


    public releng_Repository(
        String location    ) {
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public releng_BuildJob getReleng_buildjob() {
        return releng_buildjob;
    }

    public void setReleng_buildjob(releng_BuildJob releng_buildjob) {
        this.releng_buildjob = releng_buildjob;
    }
    public releng_Server getReleng_server() {
        return releng_server;
    }

    public void setReleng_server(releng_Server releng_server) {
        this.releng_server = releng_server;
    }

}
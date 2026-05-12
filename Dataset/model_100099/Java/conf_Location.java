





import java.util.List;
import java.util.ArrayList;

public class conf_Location  {

    private String name;





    private conf_Admin conf_admin;




    private conf_Session conf_session;


    public conf_Location(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public conf_Admin getConf_admin() {
        return conf_admin;
    }

    public void setConf_admin(conf_Admin conf_admin) {
        this.conf_admin = conf_admin;
    }
    public conf_Session getConf_session() {
        return conf_session;
    }

    public void setConf_session(conf_Session conf_session) {
        this.conf_session = conf_session;
    }

}
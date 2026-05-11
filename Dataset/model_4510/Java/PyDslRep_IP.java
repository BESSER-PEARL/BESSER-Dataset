





import java.util.List;
import java.util.ArrayList;

public class PyDslRep_IP extends Entity {

    private String ip;
    private String name;





    private PyDslRep_Environment pydslrep_environment;


    public PyDslRep_IP(
        String ip,        String name    ) {
        super(
        );
        this.ip = ip;
        this.name = name;
    }


    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PyDslRep_Environment getPydslrep_environment() {
        return pydslrep_environment;
    }

    public void setPydslrep_environment(PyDslRep_Environment pydslrep_environment) {
        this.pydslrep_environment = pydslrep_environment;
    }

}
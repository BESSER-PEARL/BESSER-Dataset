





import java.util.List;
import java.util.ArrayList;

public class pyrep_IP extends Entity {

    private String ip;
    private String name;





    private pyrep_Environment pyrep_environment;


    public pyrep_IP(
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

    public pyrep_Environment getPyrep_environment() {
        return pyrep_environment;
    }

    public void setPyrep_environment(pyrep_Environment pyrep_environment) {
        this.pyrep_environment = pyrep_environment;
    }

}
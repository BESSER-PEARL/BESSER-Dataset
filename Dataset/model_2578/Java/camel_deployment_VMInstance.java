





import java.util.List;
import java.util.ArrayList;

public class camel_deployment_VMInstance extends ComponentInstance {

    private String ip;



    public camel_deployment_VMInstance(
        String ip    ) {
        super(
        );
        this.ip = ip;
    }


    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }


}






import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExternalComponentInstance extends ComponentInstance {

    private String ips;
    private String status;



    public cloudml_core_ExternalComponentInstance(
        String ips,        String status    ) {
        super(
        );
        this.ips = ips;
        this.status = status;
    }


    public String getIps() {
        return ips;
    }

    public void setIps(String ips) {
        this.ips = ips;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}
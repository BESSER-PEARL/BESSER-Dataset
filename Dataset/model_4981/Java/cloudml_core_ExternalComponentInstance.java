





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExternalComponentInstance extends ComponentInstance {

    private String ips;



    public cloudml_core_ExternalComponentInstance(
        String ips    ) {
        super(
        );
        this.ips = ips;
    }


    public String getIps() {
        return ips;
    }

    public void setIps(String ips) {
        this.ips = ips;
    }


}
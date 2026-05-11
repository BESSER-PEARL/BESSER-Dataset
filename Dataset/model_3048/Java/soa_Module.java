





import java.util.List;
import java.util.ArrayList;

public class soa_Module  {

    private String event;
    private String version;
    private String name;





    private soa_Architecture soa_architecture;


    public soa_Module(
        String event,        String version,        String name    ) {
        this.event = event;
        this.version = version;
        this.name = name;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public soa_Architecture getSoa_architecture() {
        return soa_architecture;
    }

    public void setSoa_architecture(soa_Architecture soa_architecture) {
        this.soa_architecture = soa_architecture;
    }

}






import java.util.List;
import java.util.ArrayList;

public class micro_Service extends NamedElement {

    private int port;
    private String description;
    private String shortname;
    private String fullname;





    private micro_MicroserviceArchitecture micro_microservicearchitecture;


    public micro_Service(
        int port,        String description,        String shortname,        String fullname    ) {
        super(
        );
        this.port = port;
        this.description = description;
        this.shortname = shortname;
        this.fullname = fullname;
    }


    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getShortname() {
        return shortname;
    }

    public void setShortname(String shortname) {
        this.shortname = shortname;
    }
    public String getFullname() {
        return fullname;
    }

    public void setFullname(String fullname) {
        this.fullname = fullname;
    }

    public micro_MicroserviceArchitecture getMicro_microservicearchitecture() {
        return micro_microservicearchitecture;
    }

    public void setMicro_microservicearchitecture(micro_MicroserviceArchitecture micro_microservicearchitecture) {
        this.micro_microservicearchitecture = micro_microservicearchitecture;
    }

}
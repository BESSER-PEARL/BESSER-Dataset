





import java.util.List;
import java.util.ArrayList;

public class micro_Service extends NamedElement {

    private String fullname;
    private String shortname;
    private String description;
    private int port;





    private micro_MicroserviceArchitecture micro_microservicearchitecture;


    public micro_Service(
        String fullname,        String shortname,        String description,        int port    ) {
        super(
        );
        this.fullname = fullname;
        this.shortname = shortname;
        this.description = description;
        this.port = port;
    }


    public String getFullname() {
        return fullname;
    }

    public void setFullname(String fullname) {
        this.fullname = fullname;
    }
    public String getShortname() {
        return shortname;
    }

    public void setShortname(String shortname) {
        this.shortname = shortname;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public micro_MicroserviceArchitecture getMicro_microservicearchitecture() {
        return micro_microservicearchitecture;
    }

    public void setMicro_microservicearchitecture(micro_MicroserviceArchitecture micro_microservicearchitecture) {
        this.micro_microservicearchitecture = micro_microservicearchitecture;
    }

}
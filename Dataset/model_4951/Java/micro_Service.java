





import java.util.List;
import java.util.ArrayList;

public class micro_Service extends NamedElement {

    private String fullname;
    private int port;
    private String description;
    private String shortname;



    public micro_Service(
        String fullname,        int port,        String description,        String shortname    ) {
        super(
        );
        this.fullname = fullname;
        this.port = port;
        this.description = description;
        this.shortname = shortname;
    }


    public String getFullname() {
        return fullname;
    }

    public void setFullname(String fullname) {
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


}
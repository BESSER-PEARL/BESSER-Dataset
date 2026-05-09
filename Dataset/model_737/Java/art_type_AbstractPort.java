





import java.util.List;
import java.util.ArrayList;

public class art_type_AbstractPort extends NamedElement {

    private String role;
    private String protocol;
    private String uri;



    public art_type_AbstractPort(
        String role,        String protocol,        String uri    ) {
        super(
        );
        this.role = role;
        this.protocol = protocol;
        this.uri = uri;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}
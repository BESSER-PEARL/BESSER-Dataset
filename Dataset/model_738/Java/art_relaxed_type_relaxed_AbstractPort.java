





import java.util.List;
import java.util.ArrayList;

public class art_relaxed_type_relaxed_AbstractPort extends NamedElement {

    private String protocol;
    private String role;
    private String uri;



    public art_relaxed_type_relaxed_AbstractPort(
        String protocol,        String role,        String uri    ) {
        super(
        );
        this.protocol = protocol;
        this.role = role;
        this.uri = uri;
    }


    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}
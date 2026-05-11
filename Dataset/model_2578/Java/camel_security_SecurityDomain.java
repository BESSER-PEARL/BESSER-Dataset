





import java.util.List;
import java.util.ArrayList;

public class camel_security_SecurityDomain  {

    private String id;
    private String name;





    private List<SecurityDomain> securitydomains;


    public camel_security_SecurityDomain(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
        this.securitydomains = new ArrayList<>();
    }

    public camel_security_SecurityDomain(
        String id,        String name        ArrayList<SecurityDomain> securitydomains    ) {
        this.id = id;
        this.name = name;
        this.securitydomains = securitydomains;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SecurityDomain> getSecuritydomains() {
        return securitydomains;
    }

    public void addSecuritydomain(Securitydomain securitydomain) {
        this.securitydomains.add(securitydomain);
    }

}
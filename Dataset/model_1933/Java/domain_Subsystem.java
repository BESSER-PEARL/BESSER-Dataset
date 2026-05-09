





import java.util.List;
import java.util.ArrayList;

public class domain_Subsystem  {

    private String name;
    private String uid;





    private domain_Datacenter domain_datacenter;




    private domain_Datacenter domain_datacenter;


    public domain_Subsystem(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Datacenter getDomain_datacenter() {
        return domain_datacenter;
    }

    public void setDomain_datacenter(domain_Datacenter domain_datacenter) {
        this.domain_datacenter = domain_datacenter;
    }
    public domain_Datacenter getDomain_datacenter() {
        return domain_datacenter;
    }

    public void setDomain_datacenter(domain_Datacenter domain_datacenter) {
        this.domain_datacenter = domain_datacenter;
    }

}
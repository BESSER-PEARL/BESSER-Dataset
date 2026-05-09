





import java.util.List;
import java.util.ArrayList;

public class domain_InfrastructureComponent  {

    private String uid;
    private String name;





    private domain_InfrastructureConnection domain_infrastructureconnection;




    private domain_InfrastructureConnection domain_infrastructureconnection;




    private domain_InfrastructureLayer domain_infrastructurelayer;




    private domain_InfrastructureLayer domain_infrastructurelayer;


    public domain_InfrastructureComponent(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domain_InfrastructureConnection getDomain_infrastructureconnection() {
        return domain_infrastructureconnection;
    }

    public void setDomain_infrastructureconnection(domain_InfrastructureConnection domain_infrastructureconnection) {
        this.domain_infrastructureconnection = domain_infrastructureconnection;
    }
    public domain_InfrastructureConnection getDomain_infrastructureconnection() {
        return domain_infrastructureconnection;
    }

    public void setDomain_infrastructureconnection(domain_InfrastructureConnection domain_infrastructureconnection) {
        this.domain_infrastructureconnection = domain_infrastructureconnection;
    }
    public domain_InfrastructureLayer getDomain_infrastructurelayer() {
        return domain_infrastructurelayer;
    }

    public void setDomain_infrastructurelayer(domain_InfrastructureLayer domain_infrastructurelayer) {
        this.domain_infrastructurelayer = domain_infrastructurelayer;
    }
    public domain_InfrastructureLayer getDomain_infrastructurelayer() {
        return domain_infrastructurelayer;
    }

    public void setDomain_infrastructurelayer(domain_InfrastructureLayer domain_infrastructurelayer) {
        this.domain_infrastructurelayer = domain_infrastructurelayer;
    }

}






import java.util.List;
import java.util.ArrayList;

public class domain_EnterpriseInfrastructure  {

    private String uid;





    private List<domain_InfrastructureConnection> domain_infrastructureconnections;




    private domain_ApplicationInfrastructureLayer domain_applicationinfrastructurelayer;




    private domain_Datacenter domain_datacenter;




    private domain_ApplicationInfrastructureLayer domain_applicationinfrastructurelayer;




    private domain_EObject domain_eobject;




    private List<domain_Datacenter> domain_datacenters;


    public domain_EnterpriseInfrastructure(
        String uid    ) {
        this.uid = uid;
        this.domain_infrastructureconnections = new ArrayList<>();
        this.domain_datacenters = new ArrayList<>();
    }

    public domain_EnterpriseInfrastructure(
        String uid        ArrayList<domain_InfrastructureConnection> domain_infrastructureconnections,        ArrayList<domain_Datacenter> domain_datacenters    ) {
        this.uid = uid;
        this.domain_infrastructureconnections = domain_infrastructureconnections;
        this.domain_datacenters = domain_datacenters;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public List<domain_InfrastructureConnection> getDomain_infrastructureconnections() {
        return domain_infrastructureconnections;
    }

    public void addDomain_infrastructureconnection(Domain_infrastructureconnection domain_infrastructureconnection) {
        this.domain_infrastructureconnections.add(domain_infrastructureconnection);
    }
    public domain_ApplicationInfrastructureLayer getDomain_applicationinfrastructurelayer() {
        return domain_applicationinfrastructurelayer;
    }

    public void setDomain_applicationinfrastructurelayer(domain_ApplicationInfrastructureLayer domain_applicationinfrastructurelayer) {
        this.domain_applicationinfrastructurelayer = domain_applicationinfrastructurelayer;
    }
    public domain_Datacenter getDomain_datacenter() {
        return domain_datacenter;
    }

    public void setDomain_datacenter(domain_Datacenter domain_datacenter) {
        this.domain_datacenter = domain_datacenter;
    }
    public domain_ApplicationInfrastructureLayer getDomain_applicationinfrastructurelayer() {
        return domain_applicationinfrastructurelayer;
    }

    public void setDomain_applicationinfrastructurelayer(domain_ApplicationInfrastructureLayer domain_applicationinfrastructurelayer) {
        this.domain_applicationinfrastructurelayer = domain_applicationinfrastructurelayer;
    }
    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }
    public List<domain_Datacenter> getDomain_datacenters() {
        return domain_datacenters;
    }

    public void addDomain_datacenter(Domain_datacenter domain_datacenter) {
        this.domain_datacenters.add(domain_datacenter);
    }

}
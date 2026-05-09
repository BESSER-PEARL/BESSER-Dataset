





import java.util.List;
import java.util.ArrayList;

public class domain_ArtifactRef  {

    private String uid;





    private domain_Artifact domain_artifact;




    private domain_DomainArtifact domain_domainartifact;


    public domain_ArtifactRef(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Artifact getDomain_artifact() {
        return domain_artifact;
    }

    public void setDomain_artifact(domain_Artifact domain_artifact) {
        this.domain_artifact = domain_artifact;
    }
    public domain_DomainArtifact getDomain_domainartifact() {
        return domain_domainartifact;
    }

    public void setDomain_domainartifact(domain_DomainArtifact domain_domainartifact) {
        this.domain_domainartifact = domain_domainartifact;
    }

}
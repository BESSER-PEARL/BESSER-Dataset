





import java.util.List;
import java.util.ArrayList;

public class domain_ModelQuery  {

    private String query;
    private String name;
    private String uid;





    private domain_Artifact domain_artifact;




    private domain_Artifact domain_artifact;


    public domain_ModelQuery(
        String query,        String name,        String uid    ) {
        this.query = query;
        this.name = name;
        this.uid = uid;
    }


    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
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

    public domain_Artifact getDomain_artifact() {
        return domain_artifact;
    }

    public void setDomain_artifact(domain_Artifact domain_artifact) {
        this.domain_artifact = domain_artifact;
    }
    public domain_Artifact getDomain_artifact() {
        return domain_artifact;
    }

    public void setDomain_artifact(domain_Artifact domain_artifact) {
        this.domain_artifact = domain_artifact;
    }

}
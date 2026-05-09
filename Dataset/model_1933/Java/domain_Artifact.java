





import java.util.List;
import java.util.ArrayList;

public class domain_Artifact  {

    private String description;
    private String template;
    private String uid;
    private String name;





    private List<domain_GenerationHint> domain_generationhints;




    private domain_Artifacts domain_artifacts;




    private domain_Artifacts domain_artifacts;


    public domain_Artifact(
        String description,        String template,        String uid,        String name    ) {
        this.description = description;
        this.template = template;
        this.uid = uid;
        this.name = name;
        this.domain_generationhints = new ArrayList<>();
    }

    public domain_Artifact(
        String description,        String template,        String uid,        String name        ArrayList<domain_GenerationHint> domain_generationhints    ) {
        this.description = description;
        this.template = template;
        this.uid = uid;
        this.name = name;
        this.domain_generationhints = domain_generationhints;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
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

    public List<domain_GenerationHint> getDomain_generationhints() {
        return domain_generationhints;
    }

    public void addDomain_generationhint(Domain_generationhint domain_generationhint) {
        this.domain_generationhints.add(domain_generationhint);
    }
    public domain_Artifacts getDomain_artifacts() {
        return domain_artifacts;
    }

    public void setDomain_artifacts(domain_Artifacts domain_artifacts) {
        this.domain_artifacts = domain_artifacts;
    }
    public domain_Artifacts getDomain_artifacts() {
        return domain_artifacts;
    }

    public void setDomain_artifacts(domain_Artifacts domain_artifacts) {
        this.domain_artifacts = domain_artifacts;
    }

}






import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_AuditContainer  {

    private String description;
    private String id;
    private String name;





    private List<AuditRule> auditrules;




    private List<AuditContainer> auditcontainers;




    private AuditContainer auditcontainer;


    public gmf_all_mappings_AuditContainer(
        String description,        String id,        String name    ) {
        this.description = description;
        this.id = id;
        this.name = name;
        this.auditrules = new ArrayList<>();
        this.auditcontainers = new ArrayList<>();
    }

    public gmf_all_mappings_AuditContainer(
        String description,        String id,        String name        ArrayList<AuditRule> auditrules,        ArrayList<AuditContainer> auditcontainers    ) {
        this.description = description;
        this.id = id;
        this.name = name;
        this.auditrules = auditrules;
        this.auditcontainers = auditcontainers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

    public List<AuditRule> getAuditrules() {
        return auditrules;
    }

    public void addAuditrule(Auditrule auditrule) {
        this.auditrules.add(auditrule);
    }
    public List<AuditContainer> getAuditcontainers() {
        return auditcontainers;
    }

    public void addAuditcontainer(Auditcontainer auditcontainer) {
        this.auditcontainers.add(auditcontainer);
    }
    public AuditContainer getAuditcontainer() {
        return auditcontainer;
    }

    public void setAuditcontainer(AuditContainer auditcontainer) {
        this.auditcontainer = auditcontainer;
    }

}
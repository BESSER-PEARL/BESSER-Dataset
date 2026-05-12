





import java.util.List;
import java.util.ArrayList;

public class Tool extends AssessmentElement {

    private String branch;
    private None sector;
    private String target_legal_requirements;
    private String version;
    private String project;
    private String scientific_reference;
    private None verification_type;
    private None licensing;
    private String provider;
    private String project_maturity;
    private None verification_targets;
    private None target_system;





    private List<Observation> observations;


    public Tool(
        String branch,        None sector,        String target_legal_requirements,        String version,        String project,        String scientific_reference,        None verification_type,        None licensing,        String provider,        String project_maturity,        None verification_targets,        None target_system    ) {
        super(
            String,            name,            String,            description        );
        this.branch = branch;
        this.sector = sector;
        this.target_legal_requirements = target_legal_requirements;
        this.version = version;
        this.project = project;
        this.scientific_reference = scientific_reference;
        this.verification_type = verification_type;
        this.licensing = licensing;
        this.provider = provider;
        this.project_maturity = project_maturity;
        this.verification_targets = verification_targets;
        this.target_system = target_system;
        this.observations = new ArrayList<>();
    }

    public Tool(
        String branch,        None sector,        String target_legal_requirements,        String version,        String project,        String scientific_reference,        None verification_type,        None licensing,        String provider,        String project_maturity,        None verification_targets,        None target_system        ArrayList<Observation> observations    ) {
        this.branch = branch;
        this.sector = sector;
        this.target_legal_requirements = target_legal_requirements;
        this.version = version;
        this.project = project;
        this.scientific_reference = scientific_reference;
        this.verification_type = verification_type;
        this.licensing = licensing;
        this.provider = provider;
        this.project_maturity = project_maturity;
        this.verification_targets = verification_targets;
        this.target_system = target_system;
        this.observations = observations;
    }

    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
    public None getSector() {
        return sector;
    }

    public void setSector(None sector) {
        this.sector = sector;
    }
    public String getTarget_legal_requirements() {
        return target_legal_requirements;
    }

    public void setTarget_legal_requirements(String target_legal_requirements) {
        this.target_legal_requirements = target_legal_requirements;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public String getScientific_reference() {
        return scientific_reference;
    }

    public void setScientific_reference(String scientific_reference) {
        this.scientific_reference = scientific_reference;
    }
    public None getVerification_type() {
        return verification_type;
    }

    public void setVerification_type(None verification_type) {
        this.verification_type = verification_type;
    }
    public None getLicensing() {
        return licensing;
    }

    public void setLicensing(None licensing) {
        this.licensing = licensing;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getProject_maturity() {
        return project_maturity;
    }

    public void setProject_maturity(String project_maturity) {
        this.project_maturity = project_maturity;
    }
    public None getVerification_targets() {
        return verification_targets;
    }

    public void setVerification_targets(None verification_targets) {
        this.verification_targets = verification_targets;
    }
    public None getTarget_system() {
        return target_system;
    }

    public void setTarget_system(None target_system) {
        this.target_system = target_system;
    }

    public List<Observation> getObservations() {
        return observations;
    }

    public void addObservation(Observation observation) {
        this.observations.add(observation);
    }

}
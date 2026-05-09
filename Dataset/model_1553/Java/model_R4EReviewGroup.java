





import java.util.List;
import java.util.ArrayList;

public class model_R4EReviewGroup extends R4EReviewComponent, ReviewGroup {

    private String defaultEntryCriteria;
    private String availableProjects;
    private String folder;
    private String availableComponents;
    private String name;
    private String designRuleLocations;



    public model_R4EReviewGroup(
        String defaultEntryCriteria,        String availableProjects,        String folder,        String availableComponents,        String name,        String designRuleLocations    ) {
        super(
        );
        this.defaultEntryCriteria = defaultEntryCriteria;
        this.availableProjects = availableProjects;
        this.folder = folder;
        this.availableComponents = availableComponents;
        this.name = name;
        this.designRuleLocations = designRuleLocations;
    }


    public String getDefaultentrycriteria() {
        return defaultEntryCriteria;
    }

    public void setDefaultentrycriteria(String defaultEntryCriteria) {
        this.defaultEntryCriteria = defaultEntryCriteria;
    }
    public String getAvailableprojects() {
        return availableProjects;
    }

    public void setAvailableprojects(String availableProjects) {
        this.availableProjects = availableProjects;
    }
    public String getFolder() {
        return folder;
    }

    public void setFolder(String folder) {
        this.folder = folder;
    }
    public String getAvailablecomponents() {
        return availableComponents;
    }

    public void setAvailablecomponents(String availableComponents) {
        this.availableComponents = availableComponents;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDesignrulelocations() {
        return designRuleLocations;
    }

    public void setDesignrulelocations(String designRuleLocations) {
        this.designRuleLocations = designRuleLocations;
    }


}
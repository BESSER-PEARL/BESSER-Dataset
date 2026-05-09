





import java.util.List;
import java.util.ArrayList;

public class libraryElement_AutomationSystem extends LibraryElement {

    private String project;





    private List<libraryElement_Mapping> libraryelement_mappings;




    private List<libraryElement_Application> libraryelement_applications;


    public libraryElement_AutomationSystem(
        String project    ) {
        super(
        );
        this.project = project;
        this.libraryelement_mappings = new ArrayList<>();
        this.libraryelement_applications = new ArrayList<>();
    }

    public libraryElement_AutomationSystem(
        String project        ArrayList<libraryElement_Mapping> libraryelement_mappings,        ArrayList<libraryElement_Application> libraryelement_applications    ) {
        this.project = project;
        this.libraryelement_mappings = libraryelement_mappings;
        this.libraryelement_applications = libraryelement_applications;
    }

    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }

    public List<libraryElement_Mapping> getLibraryelement_mappings() {
        return libraryelement_mappings;
    }

    public void addLibraryelement_mapping(Libraryelement_mapping libraryelement_mapping) {
        this.libraryelement_mappings.add(libraryelement_mapping);
    }
    public List<libraryElement_Application> getLibraryelement_applications() {
        return libraryelement_applications;
    }

    public void addLibraryelement_application(Libraryelement_application libraryelement_application) {
        this.libraryelement_applications.add(libraryelement_application);
    }

}
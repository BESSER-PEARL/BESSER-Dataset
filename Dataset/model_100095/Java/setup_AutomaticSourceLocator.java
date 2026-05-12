





import java.util.List;
import java.util.ArrayList;

public class setup_AutomaticSourceLocator extends SourceLocator {

    private String rootFolder;
    private boolean locateNestedProjects;





    private setup_ProjectsImportTask setup_projectsimporttask;




    private setup_MavenImportTask setup_mavenimporttask;


    public setup_AutomaticSourceLocator(
        String rootFolder,        boolean locateNestedProjects    ) {
        super(
        );
        this.rootFolder = rootFolder;
        this.locateNestedProjects = locateNestedProjects;
    }


    public String getRootfolder() {
        return rootFolder;
    }

    public void setRootfolder(String rootFolder) {
        this.rootFolder = rootFolder;
    }
    public boolean getLocatenestedprojects() {
        return locateNestedProjects;
    }

    public void setLocatenestedprojects(boolean locateNestedProjects) {
        this.locateNestedProjects = locateNestedProjects;
    }

    public setup_ProjectsImportTask getSetup_projectsimporttask() {
        return setup_projectsimporttask;
    }

    public void setSetup_projectsimporttask(setup_ProjectsImportTask setup_projectsimporttask) {
        this.setup_projectsimporttask = setup_projectsimporttask;
    }
    public setup_MavenImportTask getSetup_mavenimporttask() {
        return setup_mavenimporttask;
    }

    public void setSetup_mavenimporttask(setup_MavenImportTask setup_mavenimporttask) {
        this.setup_mavenimporttask = setup_mavenimporttask;
    }

}






import java.util.List;
import java.util.ArrayList;

public class PSM_DependencyLibrary extends ArtifactElement {

    private String LibraryGroupName;
    private String LibraryName;
    private String LibraryScope;





    private PSM_MicroserviceProject psm_microserviceproject;


    public PSM_DependencyLibrary(
        String LibraryGroupName,        String LibraryName,        String LibraryScope    ) {
        super(
        );
        this.LibraryGroupName = LibraryGroupName;
        this.LibraryName = LibraryName;
        this.LibraryScope = LibraryScope;
    }


    public String getLibrarygroupname() {
        return LibraryGroupName;
    }

    public void setLibrarygroupname(String LibraryGroupName) {
        this.LibraryGroupName = LibraryGroupName;
    }
    public String getLibraryname() {
        return LibraryName;
    }

    public void setLibraryname(String LibraryName) {
        this.LibraryName = LibraryName;
    }
    public String getLibraryscope() {
        return LibraryScope;
    }

    public void setLibraryscope(String LibraryScope) {
        this.LibraryScope = LibraryScope;
    }

    public PSM_MicroserviceProject getPsm_microserviceproject() {
        return psm_microserviceproject;
    }

    public void setPsm_microserviceproject(PSM_MicroserviceProject psm_microserviceproject) {
        this.psm_microserviceproject = psm_microserviceproject;
    }

}
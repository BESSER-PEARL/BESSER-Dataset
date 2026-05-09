





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Subproject  {

    private String name;





    private List<UnifiedMetamodel__Library> unifiedmetamodel__librarys;




    private List<UnifiedMetamodel__Epackage> unifiedmetamodel__epackages;




    private UnifiedMetamodel__JEE_Project unifiedmetamodel__jee_project;


    public UnifiedMetamodel__Subproject(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__librarys = new ArrayList<>();
        this.unifiedmetamodel__epackages = new ArrayList<>();
    }

    public UnifiedMetamodel__Subproject(
        String name        ArrayList<UnifiedMetamodel__Library> unifiedmetamodel__librarys,        ArrayList<UnifiedMetamodel__Epackage> unifiedmetamodel__epackages    ) {
        this.name = name;
        this.unifiedmetamodel__librarys = unifiedmetamodel__librarys;
        this.unifiedmetamodel__epackages = unifiedmetamodel__epackages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UnifiedMetamodel__Library> getUnifiedmetamodel__librarys() {
        return unifiedmetamodel__librarys;
    }

    public void addUnifiedmetamodel__library(Unifiedmetamodel__library unifiedmetamodel__library) {
        this.unifiedmetamodel__librarys.add(unifiedmetamodel__library);
    }
    public List<UnifiedMetamodel__Epackage> getUnifiedmetamodel__epackages() {
        return unifiedmetamodel__epackages;
    }

    public void addUnifiedmetamodel__epackage(Unifiedmetamodel__epackage unifiedmetamodel__epackage) {
        this.unifiedmetamodel__epackages.add(unifiedmetamodel__epackage);
    }
    public UnifiedMetamodel__JEE_Project getUnifiedmetamodel__jee_project() {
        return unifiedmetamodel__jee_project;
    }

    public void setUnifiedmetamodel__jee_project(UnifiedMetamodel__JEE_Project unifiedmetamodel__jee_project) {
        this.unifiedmetamodel__jee_project = unifiedmetamodel__jee_project;
    }

}
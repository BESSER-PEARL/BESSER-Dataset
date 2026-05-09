





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_SingleDependencies  {






    private softGalleryLanguage_ReactDependenciesSubRules softgallerylanguage_reactdependenciessubrules;




    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;


    public softGalleryLanguage_SingleDependencies(
    ) {
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_SingleDependencies(
        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }


    public softGalleryLanguage_ReactDependenciesSubRules getSoftgallerylanguage_reactdependenciessubrules() {
        return softgallerylanguage_reactdependenciessubrules;
    }

    public void setSoftgallerylanguage_reactdependenciessubrules(softGalleryLanguage_ReactDependenciesSubRules softgallerylanguage_reactdependenciessubrules) {
        this.softgallerylanguage_reactdependenciessubrules = softgallerylanguage_reactdependenciessubrules;
    }
    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }

}
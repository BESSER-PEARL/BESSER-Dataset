





import java.util.List;
import java.util.ArrayList;

public class library_OCLPackageParent extends OCLNamedElement {






    private List<library_OCLPackage> library_oclpackages;


    public library_OCLPackageParent(
    ) {
        super(
        );
        this.library_oclpackages = new ArrayList<>();
    }

    public library_OCLPackageParent(
        ArrayList<library_OCLPackage> library_oclpackages    ) {
        this.library_oclpackages = library_oclpackages;
    }


    public List<library_OCLPackage> getLibrary_oclpackages() {
        return library_oclpackages;
    }

    public void addLibrary_oclpackage(Library_oclpackage library_oclpackage) {
        this.library_oclpackages.add(library_oclpackage);
    }

}
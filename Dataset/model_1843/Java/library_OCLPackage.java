





import java.util.List;
import java.util.ArrayList;

public class library_OCLPackage extends OCLPackageParent {






    private List<library_OCLTypeDefinition> library_ocltypedefinitions;


    public library_OCLPackage(
    ) {
        super(
        );
        this.library_ocltypedefinitions = new ArrayList<>();
    }

    public library_OCLPackage(
        ArrayList<library_OCLTypeDefinition> library_ocltypedefinitions    ) {
        this.library_ocltypedefinitions = library_ocltypedefinitions;
    }


    public List<library_OCLTypeDefinition> getLibrary_ocltypedefinitions() {
        return library_ocltypedefinitions;
    }

    public void addLibrary_ocltypedefinition(Library_ocltypedefinition library_ocltypedefinition) {
        this.library_ocltypedefinitions.add(library_ocltypedefinition);
    }

}
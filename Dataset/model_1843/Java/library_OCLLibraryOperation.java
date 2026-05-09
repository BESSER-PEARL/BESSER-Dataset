





import java.util.List;
import java.util.ArrayList;

public class library_OCLLibraryOperation extends OCLTypedElement {

    private String class_;
    private boolean isStatic;





    private library_OCLTypeDefinition library_ocltypedefinition;




    private List<library_OCLParameter> library_oclparameters;


    public library_OCLLibraryOperation(
        String class_,        boolean isStatic    ) {
        super(
        );
        this.class_ = class_;
        this.isStatic = isStatic;
        this.library_oclparameters = new ArrayList<>();
    }

    public library_OCLLibraryOperation(
        String class_,        boolean isStatic        ArrayList<library_OCLParameter> library_oclparameters    ) {
        this.class_ = class_;
        this.isStatic = isStatic;
        this.library_oclparameters = library_oclparameters;
    }

    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public library_OCLTypeDefinition getLibrary_ocltypedefinition() {
        return library_ocltypedefinition;
    }

    public void setLibrary_ocltypedefinition(library_OCLTypeDefinition library_ocltypedefinition) {
        this.library_ocltypedefinition = library_ocltypedefinition;
    }
    public List<library_OCLParameter> getLibrary_oclparameters() {
        return library_oclparameters;
    }

    public void addLibrary_oclparameter(Library_oclparameter library_oclparameter) {
        this.library_oclparameters.add(library_oclparameter);
    }

}
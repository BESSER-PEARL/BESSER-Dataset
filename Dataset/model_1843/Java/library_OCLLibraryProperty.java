





import java.util.List;
import java.util.ArrayList;

public class library_OCLLibraryProperty extends OCLTypedElement {

    private boolean isStatic;
    private String class_;





    private library_OCLTypeDefinition library_ocltypedefinition;


    public library_OCLLibraryProperty(
        boolean isStatic,        String class_    ) {
        super(
        );
        this.isStatic = isStatic;
        this.class_ = class_;
    }


    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public library_OCLTypeDefinition getLibrary_ocltypedefinition() {
        return library_ocltypedefinition;
    }

    public void setLibrary_ocltypedefinition(library_OCLTypeDefinition library_ocltypedefinition) {
        this.library_ocltypedefinition = library_ocltypedefinition;
    }

}
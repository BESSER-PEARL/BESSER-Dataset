





import java.util.List;
import java.util.ArrayList;

public class library_OCLLibraryIteration extends OCLTypedElement {

    private String iterator;
    private boolean iterators;
    private String class_;





    private library_OCLTypeDefinition library_ocltypedefinition;


    public library_OCLLibraryIteration(
        String iterator,        boolean iterators,        String class_    ) {
        super(
        );
        this.iterator = iterator;
        this.iterators = iterators;
        this.class_ = class_;
    }


    public String getIterator() {
        return iterator;
    }

    public void setIterator(String iterator) {
        this.iterator = iterator;
    }
    public boolean getIterators() {
        return iterators;
    }

    public void setIterators(boolean iterators) {
        this.iterators = iterators;
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
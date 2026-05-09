





import java.util.List;
import java.util.ArrayList;

public class libraryElement_VarDeclaration extends IInterfaceElement {

    private String arraySize;





    private libraryElement_BasicFBType libraryelement_basicfbtype;


    public libraryElement_VarDeclaration(
        String arraySize    ) {
        super(
        );
        this.arraySize = arraySize;
    }


    public String getArraysize() {
        return arraySize;
    }

    public void setArraysize(String arraySize) {
        this.arraySize = arraySize;
    }

    public libraryElement_BasicFBType getLibraryelement_basicfbtype() {
        return libraryelement_basicfbtype;
    }

    public void setLibraryelement_basicfbtype(libraryElement_BasicFBType libraryelement_basicfbtype) {
        this.libraryelement_basicfbtype = libraryelement_basicfbtype;
    }

}
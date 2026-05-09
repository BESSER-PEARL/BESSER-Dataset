





import java.util.List;
import java.util.ArrayList;

public class essentialocl_types_CollectionType extends Type {

    private String kind;





    private OclLibrary ocllibrary;


    public essentialocl_types_CollectionType(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public OclLibrary getOcllibrary() {
        return ocllibrary;
    }

    public void setOcllibrary(OclLibrary ocllibrary) {
        this.ocllibrary = ocllibrary;
    }

}
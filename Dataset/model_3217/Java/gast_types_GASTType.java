





import java.util.List;
import java.util.ArrayList;

public class gast_types_GASTType extends NamedModelElement {

    private String qualifiedName;
    private boolean referenceType;



    public gast_types_GASTType(
        String qualifiedName,        boolean referenceType    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.referenceType = referenceType;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public boolean getReferencetype() {
        return referenceType;
    }

    public void setReferencetype(boolean referenceType) {
        this.referenceType = referenceType;
    }


}
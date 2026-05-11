





import java.util.List;
import java.util.ArrayList;

public class gast_types_GASTType extends NamedModelElement {

    private boolean referenceType;
    private String qualifiedName;



    public gast_types_GASTType(
        boolean referenceType,        String qualifiedName    ) {
        super(
        );
        this.referenceType = referenceType;
        this.qualifiedName = qualifiedName;
    }


    public boolean getReferencetype() {
        return referenceType;
    }

    public void setReferencetype(boolean referenceType) {
        this.referenceType = referenceType;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }


}
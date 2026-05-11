





import java.util.List;
import java.util.ArrayList;

public class aadl2_MetaclassReference extends PropertyOwner {

    private String metaclassName;
    private String annexName;





    private aadl2_Property aadl2_property;




    private aadl2_ClassifierType aadl2_classifiertype;




    private aadl2_ReferenceType aadl2_referencetype;


    public aadl2_MetaclassReference(
        String metaclassName,        String annexName    ) {
        super(
        );
        this.metaclassName = metaclassName;
        this.annexName = annexName;
    }


    public String getMetaclassname() {
        return metaclassName;
    }

    public void setMetaclassname(String metaclassName) {
        this.metaclassName = metaclassName;
    }
    public String getAnnexname() {
        return annexName;
    }

    public void setAnnexname(String annexName) {
        this.annexName = annexName;
    }

    public aadl2_Property getAadl2_property() {
        return aadl2_property;
    }

    public void setAadl2_property(aadl2_Property aadl2_property) {
        this.aadl2_property = aadl2_property;
    }
    public aadl2_ClassifierType getAadl2_classifiertype() {
        return aadl2_classifiertype;
    }

    public void setAadl2_classifiertype(aadl2_ClassifierType aadl2_classifiertype) {
        this.aadl2_classifiertype = aadl2_classifiertype;
    }
    public aadl2_ReferenceType getAadl2_referencetype() {
        return aadl2_referencetype;
    }

    public void setAadl2_referencetype(aadl2_ReferenceType aadl2_referencetype) {
        this.aadl2_referencetype = aadl2_referencetype;
    }

}
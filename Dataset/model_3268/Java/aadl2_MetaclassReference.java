





import java.util.List;
import java.util.ArrayList;

public class aadl2_MetaclassReference extends PropertyOwner {

    private String metaclassName;
    private String annexName;





    private aadl2_Property aadl2_property;


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

}
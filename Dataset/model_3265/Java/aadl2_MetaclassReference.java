





import java.util.List;
import java.util.ArrayList;

public class aadl2_MetaclassReference extends PropertyOwner {

    private String metaclassName;
    private String annexName;



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


}
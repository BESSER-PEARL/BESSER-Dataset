





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_PackageImport extends DirectedRelationship {

    private String visibility;





    private UML2WithID_Package uml2withid_package;


    public UML2WithID_PackageImport(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UML2WithID_Package getUml2withid_package() {
        return uml2withid_package;
    }

    public void setUml2withid_package(UML2WithID_Package uml2withid_package) {
        this.uml2withid_package = uml2withid_package;
    }

}
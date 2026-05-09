





import java.util.List;
import java.util.ArrayList;

public class UML2_PackageImport extends DirectedRelationship {

    private String visibility;





    private UML2_Package uml2_package;


    public UML2_PackageImport(
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

    public UML2_Package getUml2_package() {
        return uml2_package;
    }

    public void setUml2_package(UML2_Package uml2_package) {
        this.uml2_package = uml2_package;
    }

}






import java.util.List;
import java.util.ArrayList;

public class UML2_Manifestation extends Abstraction {






    private UML2_PackageableElement uml2_packageableelement;




    private UML2_Artifact uml2_artifact;


    public UML2_Manifestation(
    ) {
        super(
        );
    }



    public UML2_PackageableElement getUml2_packageableelement() {
        return uml2_packageableelement;
    }

    public void setUml2_packageableelement(UML2_PackageableElement uml2_packageableelement) {
        this.uml2_packageableelement = uml2_packageableelement;
    }
    public UML2_Artifact getUml2_artifact() {
        return uml2_artifact;
    }

    public void setUml2_artifact(UML2_Artifact uml2_artifact) {
        this.uml2_artifact = uml2_artifact;
    }

}
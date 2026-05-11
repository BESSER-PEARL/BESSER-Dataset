





import java.util.List;
import java.util.ArrayList;

public class uml2CD_ElementImport extends DirectRelationship {

    private String visibility;





    private uml2CD_PackageableElement uml2cd_packageableelement;




    private uml2CD_Namespace uml2cd_namespace;




    private uml2CD_Namespace uml2cd_namespace;


    public uml2CD_ElementImport(
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

    public uml2CD_PackageableElement getUml2cd_packageableelement() {
        return uml2cd_packageableelement;
    }

    public void setUml2cd_packageableelement(uml2CD_PackageableElement uml2cd_packageableelement) {
        this.uml2cd_packageableelement = uml2cd_packageableelement;
    }
    public uml2CD_Namespace getUml2cd_namespace() {
        return uml2cd_namespace;
    }

    public void setUml2cd_namespace(uml2CD_Namespace uml2cd_namespace) {
        this.uml2cd_namespace = uml2cd_namespace;
    }
    public uml2CD_Namespace getUml2cd_namespace() {
        return uml2cd_namespace;
    }

    public void setUml2cd_namespace(uml2CD_Namespace uml2cd_namespace) {
        this.uml2cd_namespace = uml2cd_namespace;
    }

}
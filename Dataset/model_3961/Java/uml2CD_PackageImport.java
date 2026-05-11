





import java.util.List;
import java.util.ArrayList;

public class uml2CD_PackageImport extends DirectRelationship {

    private String visibility;





    private uml2CD_Namespace uml2cd_namespace;




    private uml2CD_Package uml2cd_package;




    private uml2CD_Namespace uml2cd_namespace;


    public uml2CD_PackageImport(
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

    public uml2CD_Namespace getUml2cd_namespace() {
        return uml2cd_namespace;
    }

    public void setUml2cd_namespace(uml2CD_Namespace uml2cd_namespace) {
        this.uml2cd_namespace = uml2cd_namespace;
    }
    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public uml2CD_Namespace getUml2cd_namespace() {
        return uml2cd_namespace;
    }

    public void setUml2cd_namespace(uml2CD_Namespace uml2cd_namespace) {
        this.uml2cd_namespace = uml2cd_namespace;
    }

}
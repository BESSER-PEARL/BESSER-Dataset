





import java.util.List;
import java.util.ArrayList;

public class cmof_ElementImport extends DirectedRelationship {

    private String visibility;
    private String alias;





    private cmof_Namespace cmof_namespace;




    private cmof_PackageableElement cmof_packageableelement;




    private cmof_Namespace cmof_namespace;


    public cmof_ElementImport(
        String visibility,        String alias    ) {
        super(
        );
        this.visibility = visibility;
        this.alias = alias;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }
    public cmof_PackageableElement getCmof_packageableelement() {
        return cmof_packageableelement;
    }

    public void setCmof_packageableelement(cmof_PackageableElement cmof_packageableelement) {
        this.cmof_packageableelement = cmof_packageableelement;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }

}
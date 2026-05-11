





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_ElementImport extends DirectedRelationship {

    private String alias;
    private String visibility;





    private Namespace namespace;




    private PackageableElement packageableelement;


    public Classes_Kernel_ElementImport(
        String alias,        String visibility    ) {
        super(
        );
        this.alias = alias;
        this.visibility = visibility;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public Namespace getNamespace() {
        return namespace;
    }

    public void setNamespace(Namespace namespace) {
        this.namespace = namespace;
    }
    public PackageableElement getPackageableelement() {
        return packageableelement;
    }

    public void setPackageableelement(PackageableElement packageableelement) {
        this.packageableelement = packageableelement;
    }

}
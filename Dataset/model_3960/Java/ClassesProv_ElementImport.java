





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_ElementImport extends DirectedRelationship {

    private String alias;





    private ClassesProv_Namespace classesprov_namespace;




    private ClassesProv_PackageableElement classesprov_packageableelement;




    private ClassesProv_Namespace classesprov_namespace;


    public ClassesProv_ElementImport(
        String alias    ) {
        super(
        );
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public ClassesProv_Namespace getClassesprov_namespace() {
        return classesprov_namespace;
    }

    public void setClassesprov_namespace(ClassesProv_Namespace classesprov_namespace) {
        this.classesprov_namespace = classesprov_namespace;
    }
    public ClassesProv_PackageableElement getClassesprov_packageableelement() {
        return classesprov_packageableelement;
    }

    public void setClassesprov_packageableelement(ClassesProv_PackageableElement classesprov_packageableelement) {
        this.classesprov_packageableelement = classesprov_packageableelement;
    }
    public ClassesProv_Namespace getClassesprov_namespace() {
        return classesprov_namespace;
    }

    public void setClassesprov_namespace(ClassesProv_Namespace classesprov_namespace) {
        this.classesprov_namespace = classesprov_namespace;
    }

}






import java.util.List;
import java.util.ArrayList;

public class classes_ElementImport extends Element {

    private String visibility;
    private String alias;





    private classes_PackageableElement classes_packageableelement;




    private classes_Namespace classes_namespace;




    private classes_Namespace classes_namespace;


    public classes_ElementImport(
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

    public classes_PackageableElement getClasses_packageableelement() {
        return classes_packageableelement;
    }

    public void setClasses_packageableelement(classes_PackageableElement classes_packageableelement) {
        this.classes_packageableelement = classes_packageableelement;
    }
    public classes_Namespace getClasses_namespace() {
        return classes_namespace;
    }

    public void setClasses_namespace(classes_Namespace classes_namespace) {
        this.classes_namespace = classes_namespace;
    }
    public classes_Namespace getClasses_namespace() {
        return classes_namespace;
    }

    public void setClasses_namespace(classes_Namespace classes_namespace) {
        this.classes_namespace = classes_namespace;
    }

}
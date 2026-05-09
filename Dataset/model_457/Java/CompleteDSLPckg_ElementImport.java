





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ElementImport extends DirectedRelationship {

    private String alias;
    private String visibility;





    private CompleteDSLPckg_PackageableElement completedslpckg_packageableelement;




    private CompleteDSLPckg_Namespace completedslpckg_namespace;




    private CompleteDSLPckg_Namespace completedslpckg_namespace;


    public CompleteDSLPckg_ElementImport(
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

    public CompleteDSLPckg_PackageableElement getCompletedslpckg_packageableelement() {
        return completedslpckg_packageableelement;
    }

    public void setCompletedslpckg_packageableelement(CompleteDSLPckg_PackageableElement completedslpckg_packageableelement) {
        this.completedslpckg_packageableelement = completedslpckg_packageableelement;
    }
    public CompleteDSLPckg_Namespace getCompletedslpckg_namespace() {
        return completedslpckg_namespace;
    }

    public void setCompletedslpckg_namespace(CompleteDSLPckg_Namespace completedslpckg_namespace) {
        this.completedslpckg_namespace = completedslpckg_namespace;
    }
    public CompleteDSLPckg_Namespace getCompletedslpckg_namespace() {
        return completedslpckg_namespace;
    }

    public void setCompletedslpckg_namespace(CompleteDSLPckg_Namespace completedslpckg_namespace) {
        this.completedslpckg_namespace = completedslpckg_namespace;
    }

}
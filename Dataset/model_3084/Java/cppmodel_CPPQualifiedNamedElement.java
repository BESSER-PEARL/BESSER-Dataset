





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPQualifiedNamedElement extends CPPNamedElement {

    private String cppQualifiedName;
    private String cppPrefix;





    private List<cppmodel_CPPQualifiedNamedElement> cppmodel_cppqualifiednamedelements;


    public cppmodel_CPPQualifiedNamedElement(
        String cppQualifiedName,        String cppPrefix    ) {
        super(
        );
        this.cppQualifiedName = cppQualifiedName;
        this.cppPrefix = cppPrefix;
        this.cppmodel_cppqualifiednamedelements = new ArrayList<>();
    }

    public cppmodel_CPPQualifiedNamedElement(
        String cppQualifiedName,        String cppPrefix        ArrayList<cppmodel_CPPQualifiedNamedElement> cppmodel_cppqualifiednamedelements    ) {
        this.cppQualifiedName = cppQualifiedName;
        this.cppPrefix = cppPrefix;
        this.cppmodel_cppqualifiednamedelements = cppmodel_cppqualifiednamedelements;
    }

    public String getCppqualifiedname() {
        return cppQualifiedName;
    }

    public void setCppqualifiedname(String cppQualifiedName) {
        this.cppQualifiedName = cppQualifiedName;
    }
    public String getCppprefix() {
        return cppPrefix;
    }

    public void setCppprefix(String cppPrefix) {
        this.cppPrefix = cppPrefix;
    }

    public List<cppmodel_CPPQualifiedNamedElement> getCppmodel_cppqualifiednamedelements() {
        return cppmodel_cppqualifiednamedelements;
    }

    public void addCppmodel_cppqualifiednamedelement(Cppmodel_cppqualifiednamedelement cppmodel_cppqualifiednamedelement) {
        this.cppmodel_cppqualifiednamedelements.add(cppmodel_cppqualifiednamedelement);
    }

}
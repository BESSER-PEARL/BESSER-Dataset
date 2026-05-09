





import java.util.List;
import java.util.ArrayList;

public class UMLModel_NamedElement extends Element {

    private String name;
    private String visibility;
    private String namespace;
    private String clientDependency;
    private String qualifiedName;



    public UMLModel_NamedElement(
        String name,        String visibility,        String namespace,        String clientDependency,        String qualifiedName    ) {
        super(
        );
        this.name = name;
        this.visibility = visibility;
        this.namespace = namespace;
        this.clientDependency = clientDependency;
        this.qualifiedName = qualifiedName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getClientdependency() {
        return clientDependency;
    }

    public void setClientdependency(String clientDependency) {
        this.clientDependency = clientDependency;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }


}






import java.util.List;
import java.util.ArrayList;

public class aadl2_NamedElement extends Element {

    private String name;
    private String qualifiedName;





    private aadl2_Namespace aadl2_namespace;




    private aadl2_Namespace aadl2_namespace;


    public aadl2_NamedElement(
        String name,        String qualifiedName    ) {
        super(
        );
        this.name = name;
        this.qualifiedName = qualifiedName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public aadl2_Namespace getAadl2_namespace() {
        return aadl2_namespace;
    }

    public void setAadl2_namespace(aadl2_Namespace aadl2_namespace) {
        this.aadl2_namespace = aadl2_namespace;
    }
    public aadl2_Namespace getAadl2_namespace() {
        return aadl2_namespace;
    }

    public void setAadl2_namespace(aadl2_Namespace aadl2_namespace) {
        this.aadl2_namespace = aadl2_namespace;
    }

}
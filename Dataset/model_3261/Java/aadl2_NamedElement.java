





import java.util.List;
import java.util.ArrayList;

public class aadl2_NamedElement extends Element {

    private String name;
    private String qualifiedName;



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


}






import java.util.List;
import java.util.ArrayList;

public class ClassesProv_NamedElement extends Element {

    private String qualifiedName;
    private String name;



    public ClassesProv_NamedElement(
        String qualifiedName,        String name    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.name = name;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
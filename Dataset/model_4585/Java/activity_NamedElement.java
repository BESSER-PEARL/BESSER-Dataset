





import java.util.List;
import java.util.ArrayList;

public class activity_NamedElement  {

    private String qualifiedName;
    private String Name;



    public activity_NamedElement(
        String qualifiedName,        String Name    ) {
        this.qualifiedName = qualifiedName;
        this.Name = Name;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}
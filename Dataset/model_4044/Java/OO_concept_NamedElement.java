





import java.util.List;
import java.util.ArrayList;

public class OO_concept_NamedElement  {

    private boolean isAbstract;
    private String name;
    private String visibility;



    public OO_concept_NamedElement(
        boolean isAbstract,        String name,        String visibility    ) {
        this.isAbstract = isAbstract;
        this.name = name;
        this.visibility = visibility;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
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


}






import java.util.List;
import java.util.ArrayList;

public class uml_NamedElement  {

    private String visibility;
    private String name;





    private uml_Dependency uml_dependency;


    public uml_NamedElement(
        String visibility,        String name    ) {
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public uml_Dependency getUml_dependency() {
        return uml_dependency;
    }

    public void setUml_dependency(uml_Dependency uml_dependency) {
        this.uml_dependency = uml_dependency;
    }

}
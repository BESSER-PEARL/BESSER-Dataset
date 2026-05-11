





import java.util.List;
import java.util.ArrayList;

public class UML_Classifier  {

    private String name;





    private UML_Package uml_package;


    public UML_Classifier(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UML_Package getUml_package() {
        return uml_package;
    }

    public void setUml_package(UML_Package uml_package) {
        this.uml_package = uml_package;
    }

}
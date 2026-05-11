





import java.util.List;
import java.util.ArrayList;

public class classDiagram_ModelingConcept  {

    private String name;





    private classDiagram_Package classdiagram_package;


    public classDiagram_ModelingConcept(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classDiagram_Package getClassdiagram_package() {
        return classdiagram_package;
    }

    public void setClassdiagram_package(classDiagram_Package classdiagram_package) {
        this.classdiagram_package = classdiagram_package;
    }

}
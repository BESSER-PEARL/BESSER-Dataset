





import java.util.List;
import java.util.ArrayList;

public class classDiagram_UMLIncrement extends UMLElement {






    private List<classDiagram_UMLStereotype> classdiagram_umlstereotypes;




    private classDiagram_UMLStereotype classdiagram_umlstereotype;


    public classDiagram_UMLIncrement(
    ) {
        super(
        );
        this.classdiagram_umlstereotypes = new ArrayList<>();
    }

    public classDiagram_UMLIncrement(
        ArrayList<classDiagram_UMLStereotype> classdiagram_umlstereotypes    ) {
        this.classdiagram_umlstereotypes = classdiagram_umlstereotypes;
    }


    public List<classDiagram_UMLStereotype> getClassdiagram_umlstereotypes() {
        return classdiagram_umlstereotypes;
    }

    public void addClassdiagram_umlstereotype(Classdiagram_umlstereotype classdiagram_umlstereotype) {
        this.classdiagram_umlstereotypes.add(classdiagram_umlstereotype);
    }
    public classDiagram_UMLStereotype getClassdiagram_umlstereotype() {
        return classdiagram_umlstereotype;
    }

    public void setClassdiagram_umlstereotype(classDiagram_UMLStereotype classdiagram_umlstereotype) {
        this.classdiagram_umlstereotype = classdiagram_umlstereotype;
    }

}
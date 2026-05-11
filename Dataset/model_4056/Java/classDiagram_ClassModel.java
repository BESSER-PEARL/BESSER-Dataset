





import java.util.List;
import java.util.ArrayList;

public class classDiagram_ClassModel  {






    private List<classDiagram_Type> classdiagram_types;


    public classDiagram_ClassModel(
    ) {
        this.classdiagram_types = new ArrayList<>();
    }

    public classDiagram_ClassModel(
        ArrayList<classDiagram_Type> classdiagram_types    ) {
        this.classdiagram_types = classdiagram_types;
    }


    public List<classDiagram_Type> getClassdiagram_types() {
        return classdiagram_types;
    }

    public void addClassdiagram_type(Classdiagram_type classdiagram_type) {
        this.classdiagram_types.add(classdiagram_type);
    }

}
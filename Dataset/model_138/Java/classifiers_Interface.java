





import java.util.List;
import java.util.ArrayList;

public class classifiers_Interface extends ConcreteClassifier {






    private List<TypeReference> typereferences;




    private List<TypeReference> typereferences;


    public classifiers_Interface(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
        this.typereferences = new ArrayList<>();
    }

    public classifiers_Interface(
        ArrayList<TypeReference> typereferences,        ArrayList<TypeReference> typereferences    ) {
        this.typereferences = typereferences;
        this.typereferences = typereferences;
    }


    public List<TypeReference> getTypereferences() {
        return typereferences;
    }

    public void addTypereference(Typereference typereference) {
        this.typereferences.add(typereference);
    }
    public List<TypeReference> getTypereferences() {
        return typereferences;
    }

    public void addTypereference(Typereference typereference) {
        this.typereferences.add(typereference);
    }

}
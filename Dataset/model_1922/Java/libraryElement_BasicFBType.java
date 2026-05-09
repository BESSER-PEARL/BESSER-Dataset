





import java.util.List;
import java.util.ArrayList;

public class libraryElement_BasicFBType extends FBType {






    private List<libraryElement_Algorithm> libraryelement_algorithms;


    public libraryElement_BasicFBType(
    ) {
        super(
        );
        this.libraryelement_algorithms = new ArrayList<>();
    }

    public libraryElement_BasicFBType(
        ArrayList<libraryElement_Algorithm> libraryelement_algorithms    ) {
        this.libraryelement_algorithms = libraryelement_algorithms;
    }


    public List<libraryElement_Algorithm> getLibraryelement_algorithms() {
        return libraryelement_algorithms;
    }

    public void addLibraryelement_algorithm(Libraryelement_algorithm libraryelement_algorithm) {
        this.libraryelement_algorithms.add(libraryelement_algorithm);
    }

}
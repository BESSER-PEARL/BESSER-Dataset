





import java.util.List;
import java.util.ArrayList;

public class simTL4J_containers_CompilationUnit extends JavaRoot {






    private List<ConcreteClassifier> concreteclassifiers;


    public simTL4J_containers_CompilationUnit(
    ) {
        super(
        );
        this.concreteclassifiers = new ArrayList<>();
    }

    public simTL4J_containers_CompilationUnit(
        ArrayList<ConcreteClassifier> concreteclassifiers    ) {
        this.concreteclassifiers = concreteclassifiers;
    }


    public List<ConcreteClassifier> getConcreteclassifiers() {
        return concreteclassifiers;
    }

    public void addConcreteclassifier(Concreteclassifier concreteclassifier) {
        this.concreteclassifiers.add(concreteclassifier);
    }

}
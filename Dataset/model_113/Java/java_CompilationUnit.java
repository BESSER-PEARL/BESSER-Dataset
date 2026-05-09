





import java.util.List;
import java.util.ArrayList;

public class java_CompilationUnit extends JavaRoot {






    private List<java_ConcreteClassifier> java_concreteclassifiers;


    public java_CompilationUnit(
    ) {
        super(
        );
        this.java_concreteclassifiers = new ArrayList<>();
    }

    public java_CompilationUnit(
        ArrayList<java_ConcreteClassifier> java_concreteclassifiers    ) {
        this.java_concreteclassifiers = java_concreteclassifiers;
    }


    public List<java_ConcreteClassifier> getJava_concreteclassifiers() {
        return java_concreteclassifiers;
    }

    public void addJava_concreteclassifier(Java_concreteclassifier java_concreteclassifier) {
        this.java_concreteclassifiers.add(java_concreteclassifier);
    }

}
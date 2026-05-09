





import java.util.List;
import java.util.ArrayList;

public class java_Enumeration extends ConcreteClassifier, Implementor {






    private List<java_EnumConstant> java_enumconstants;


    public java_Enumeration(
    ) {
        super(
        );
        this.java_enumconstants = new ArrayList<>();
    }

    public java_Enumeration(
        ArrayList<java_EnumConstant> java_enumconstants    ) {
        this.java_enumconstants = java_enumconstants;
    }


    public List<java_EnumConstant> getJava_enumconstants() {
        return java_enumconstants;
    }

    public void addJava_enumconstant(Java_enumconstant java_enumconstant) {
        this.java_enumconstants.add(java_enumconstant);
    }

}
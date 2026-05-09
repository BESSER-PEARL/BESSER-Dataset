





import java.util.List;
import java.util.ArrayList;

public class java_LocalVariable extends Variable, Initializable, AnnotableAndModifiable, ForLoopInitializer {






    private java_LocalVariableStatement java_localvariablestatement;




    private List<java_AdditionalLocalVariable> java_additionallocalvariables;


    public java_LocalVariable(
    ) {
        super(
        );
        this.java_additionallocalvariables = new ArrayList<>();
    }

    public java_LocalVariable(
        ArrayList<java_AdditionalLocalVariable> java_additionallocalvariables    ) {
        this.java_additionallocalvariables = java_additionallocalvariables;
    }


    public java_LocalVariableStatement getJava_localvariablestatement() {
        return java_localvariablestatement;
    }

    public void setJava_localvariablestatement(java_LocalVariableStatement java_localvariablestatement) {
        this.java_localvariablestatement = java_localvariablestatement;
    }
    public List<java_AdditionalLocalVariable> getJava_additionallocalvariables() {
        return java_additionallocalvariables;
    }

    public void addJava_additionallocalvariable(Java_additionallocalvariable java_additionallocalvariable) {
        this.java_additionallocalvariables.add(java_additionallocalvariable);
    }

}
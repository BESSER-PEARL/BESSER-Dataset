





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Association  {

    private int sourceMultiplicity;
    private String name;
    private int targetMultiplicity;





    private classdiagram_Class classdiagram_class;




    private classdiagram_Class classdiagram_class;


    public classdiagram_Association(
        int sourceMultiplicity,        String name,        int targetMultiplicity    ) {
        this.sourceMultiplicity = sourceMultiplicity;
        this.name = name;
        this.targetMultiplicity = targetMultiplicity;
    }


    public int getSourcemultiplicity() {
        return sourceMultiplicity;
    }

    public void setSourcemultiplicity(int sourceMultiplicity) {
        this.sourceMultiplicity = sourceMultiplicity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTargetmultiplicity() {
        return targetMultiplicity;
    }

    public void setTargetmultiplicity(int targetMultiplicity) {
        this.targetMultiplicity = targetMultiplicity;
    }

    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }

}






import java.util.List;
import java.util.ArrayList;

public class classdiagram_Attribute  {

    private String name;
    private boolean is_primary;





    private classdiagram_Class classdiagram_class;




    private classdiagram_Classifier classdiagram_classifier;


    public classdiagram_Attribute(
        String name,        boolean is_primary    ) {
        this.name = name;
        this.is_primary = is_primary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }

    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public classdiagram_Classifier getClassdiagram_classifier() {
        return classdiagram_classifier;
    }

    public void setClassdiagram_classifier(classdiagram_Classifier classdiagram_classifier) {
        this.classdiagram_classifier = classdiagram_classifier;
    }

}
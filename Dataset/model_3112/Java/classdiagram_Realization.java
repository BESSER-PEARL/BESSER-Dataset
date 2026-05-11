





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Realization  {






    private classdiagram_Class classdiagram_class;




    private List<classdiagram_Class> classdiagram_classs;


    public classdiagram_Realization(
    ) {
        this.classdiagram_classs = new ArrayList<>();
    }

    public classdiagram_Realization(
        ArrayList<classdiagram_Class> classdiagram_classs    ) {
        this.classdiagram_classs = classdiagram_classs;
    }


    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public List<classdiagram_Class> getClassdiagram_classs() {
        return classdiagram_classs;
    }

    public void addClassdiagram_class(Classdiagram_class classdiagram_class) {
        this.classdiagram_classs.add(classdiagram_class);
    }

}
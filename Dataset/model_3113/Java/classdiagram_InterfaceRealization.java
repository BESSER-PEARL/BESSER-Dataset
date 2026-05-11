





import java.util.List;
import java.util.ArrayList;

public class classdiagram_InterfaceRealization  {






    private List<classdiagram_Class> classdiagram_classs;


    public classdiagram_InterfaceRealization(
    ) {
        this.classdiagram_classs = new ArrayList<>();
    }

    public classdiagram_InterfaceRealization(
        ArrayList<classdiagram_Class> classdiagram_classs    ) {
        this.classdiagram_classs = classdiagram_classs;
    }


    public List<classdiagram_Class> getClassdiagram_classs() {
        return classdiagram_classs;
    }

    public void addClassdiagram_class(Classdiagram_class classdiagram_class) {
        this.classdiagram_classs.add(classdiagram_class);
    }

}
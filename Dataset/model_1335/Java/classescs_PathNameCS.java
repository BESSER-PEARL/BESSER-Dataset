





import java.util.List;
import java.util.ArrayList;

public class classescs_PathNameCS  {






    private classescs_ClassCS classescs_classcs;




    private List<classescs_PathElementCS> classescs_pathelementcss;


    public classescs_PathNameCS(
    ) {
        this.classescs_pathelementcss = new ArrayList<>();
    }

    public classescs_PathNameCS(
        ArrayList<classescs_PathElementCS> classescs_pathelementcss    ) {
        this.classescs_pathelementcss = classescs_pathelementcss;
    }


    public classescs_ClassCS getClassescs_classcs() {
        return classescs_classcs;
    }

    public void setClassescs_classcs(classescs_ClassCS classescs_classcs) {
        this.classescs_classcs = classescs_classcs;
    }
    public List<classescs_PathElementCS> getClassescs_pathelementcss() {
        return classescs_pathelementcss;
    }

    public void addClassescs_pathelementcs(Classescs_pathelementcs classescs_pathelementcs) {
        this.classescs_pathelementcss.add(classescs_pathelementcs);
    }

}






import java.util.List;
import java.util.ArrayList;

public class classescs_PackageCS extends NamedElementCS {






    private List<classescs_ClassCS> classescs_classcss;




    private classescs_RootCS classescs_rootcs;


    public classescs_PackageCS(
    ) {
        super(
        );
        this.classescs_classcss = new ArrayList<>();
    }

    public classescs_PackageCS(
        ArrayList<classescs_ClassCS> classescs_classcss    ) {
        this.classescs_classcss = classescs_classcss;
    }


    public List<classescs_ClassCS> getClassescs_classcss() {
        return classescs_classcss;
    }

    public void addClassescs_classcs(Classescs_classcs classescs_classcs) {
        this.classescs_classcss.add(classescs_classcs);
    }
    public classescs_RootCS getClassescs_rootcs() {
        return classescs_rootcs;
    }

    public void setClassescs_rootcs(classescs_RootCS classescs_rootcs) {
        this.classescs_rootcs = classescs_rootcs;
    }

}
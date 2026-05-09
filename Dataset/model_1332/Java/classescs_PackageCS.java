





import java.util.List;
import java.util.ArrayList;

public class classescs_PackageCS extends NamedElementCS {






    private classescs_RootCS classescs_rootcs;




    private List<classescs_PackageCS> classescs_packagecss;


    public classescs_PackageCS(
    ) {
        super(
        );
        this.classescs_packagecss = new ArrayList<>();
    }

    public classescs_PackageCS(
        ArrayList<classescs_PackageCS> classescs_packagecss    ) {
        this.classescs_packagecss = classescs_packagecss;
    }


    public classescs_RootCS getClassescs_rootcs() {
        return classescs_rootcs;
    }

    public void setClassescs_rootcs(classescs_RootCS classescs_rootcs) {
        this.classescs_rootcs = classescs_rootcs;
    }
    public List<classescs_PackageCS> getClassescs_packagecss() {
        return classescs_packagecss;
    }

    public void addClassescs_packagecs(Classescs_packagecs classescs_packagecs) {
        this.classescs_packagecss.add(classescs_packagecs);
    }

}
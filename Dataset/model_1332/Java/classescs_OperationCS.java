





import java.util.List;
import java.util.ArrayList;

public class classescs_OperationCS extends NamedElementCS {

    private String params;





    private List<classescs_NameExpCS> classescs_nameexpcss;




    private classescs_ClassCS classescs_classcs;




    private classescs_PathNameCS classescs_pathnamecs;


    public classescs_OperationCS(
        String params    ) {
        super(
        );
        this.params = params;
        this.classescs_nameexpcss = new ArrayList<>();
    }

    public classescs_OperationCS(
        String params        ArrayList<classescs_NameExpCS> classescs_nameexpcss    ) {
        this.params = params;
        this.classescs_nameexpcss = classescs_nameexpcss;
    }

    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }

    public List<classescs_NameExpCS> getClassescs_nameexpcss() {
        return classescs_nameexpcss;
    }

    public void addClassescs_nameexpcs(Classescs_nameexpcs classescs_nameexpcs) {
        this.classescs_nameexpcss.add(classescs_nameexpcs);
    }
    public classescs_ClassCS getClassescs_classcs() {
        return classescs_classcs;
    }

    public void setClassescs_classcs(classescs_ClassCS classescs_classcs) {
        this.classescs_classcs = classescs_classcs;
    }
    public classescs_PathNameCS getClassescs_pathnamecs() {
        return classescs_pathnamecs;
    }

    public void setClassescs_pathnamecs(classescs_PathNameCS classescs_pathnamecs) {
        this.classescs_pathnamecs = classescs_pathnamecs;
    }

}
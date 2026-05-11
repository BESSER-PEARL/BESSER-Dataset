





import java.util.List;
import java.util.ArrayList;

public class lobj_ModuleFolder extends LearningObject {






    private lobj_ModuleFolder lobj_modulefolder;




    private List<lobj_Module> lobj_modules;


    public lobj_ModuleFolder(
    ) {
        super(
        );
        this.lobj_modules = new ArrayList<>();
    }

    public lobj_ModuleFolder(
        ArrayList<lobj_Module> lobj_modules    ) {
        this.lobj_modules = lobj_modules;
    }


    public lobj_ModuleFolder getLobj_modulefolder() {
        return lobj_modulefolder;
    }

    public void setLobj_modulefolder(lobj_ModuleFolder lobj_modulefolder) {
        this.lobj_modulefolder = lobj_modulefolder;
    }
    public List<lobj_Module> getLobj_modules() {
        return lobj_modules;
    }

    public void addLobj_module(Lobj_module lobj_module) {
        this.lobj_modules.add(lobj_module);
    }

}
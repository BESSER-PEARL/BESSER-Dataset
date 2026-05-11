





import java.util.List;
import java.util.ArrayList;

public class lobj_ResrcFolder extends LearningObject {

    private boolean deleteScheduled;





    private List<lobj_ResrcFile> lobj_resrcfiles;




    private List<lobj_ResrcFolder> lobj_resrcfolders;


    public lobj_ResrcFolder(
        boolean deleteScheduled    ) {
        super(
        );
        this.deleteScheduled = deleteScheduled;
        this.lobj_resrcfiles = new ArrayList<>();
        this.lobj_resrcfolders = new ArrayList<>();
    }

    public lobj_ResrcFolder(
        boolean deleteScheduled        ArrayList<lobj_ResrcFile> lobj_resrcfiles,        ArrayList<lobj_ResrcFolder> lobj_resrcfolders    ) {
        this.deleteScheduled = deleteScheduled;
        this.lobj_resrcfiles = lobj_resrcfiles;
        this.lobj_resrcfolders = lobj_resrcfolders;
    }

    public boolean getDeletescheduled() {
        return deleteScheduled;
    }

    public void setDeletescheduled(boolean deleteScheduled) {
        this.deleteScheduled = deleteScheduled;
    }

    public List<lobj_ResrcFile> getLobj_resrcfiles() {
        return lobj_resrcfiles;
    }

    public void addLobj_resrcfile(Lobj_resrcfile lobj_resrcfile) {
        this.lobj_resrcfiles.add(lobj_resrcfile);
    }
    public List<lobj_ResrcFolder> getLobj_resrcfolders() {
        return lobj_resrcfolders;
    }

    public void addLobj_resrcfolder(Lobj_resrcfolder lobj_resrcfolder) {
        this.lobj_resrcfolders.add(lobj_resrcfolder);
    }

}
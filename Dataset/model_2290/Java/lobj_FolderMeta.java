




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_FolderMeta extends LearningObject {

    private LocalDate creationDate;
    private String title;
    private String description;





    private lobj_ResrcFolder lobj_resrcfolder;




    private lobj_LuFolder lobj_lufolder;




    private lobj_ModuleFolder lobj_modulefolder;


    public lobj_FolderMeta(
        LocalDate creationDate,        String title,        String description    ) {
        super(
        );
        this.creationDate = creationDate;
        this.title = title;
        this.description = description;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public lobj_ResrcFolder getLobj_resrcfolder() {
        return lobj_resrcfolder;
    }

    public void setLobj_resrcfolder(lobj_ResrcFolder lobj_resrcfolder) {
        this.lobj_resrcfolder = lobj_resrcfolder;
    }
    public lobj_LuFolder getLobj_lufolder() {
        return lobj_lufolder;
    }

    public void setLobj_lufolder(lobj_LuFolder lobj_lufolder) {
        this.lobj_lufolder = lobj_lufolder;
    }
    public lobj_ModuleFolder getLobj_modulefolder() {
        return lobj_modulefolder;
    }

    public void setLobj_modulefolder(lobj_ModuleFolder lobj_modulefolder) {
        this.lobj_modulefolder = lobj_modulefolder;
    }

}
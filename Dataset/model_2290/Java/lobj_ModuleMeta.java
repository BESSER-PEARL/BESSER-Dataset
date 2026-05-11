




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_ModuleMeta extends LearningObject {

    private LocalDate creationDate;





    private lobj_Module lobj_module;




    private lobj_Language lobj_language;


    public lobj_ModuleMeta(
        LocalDate creationDate    ) {
        super(
        );
        this.creationDate = creationDate;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public lobj_Module getLobj_module() {
        return lobj_module;
    }

    public void setLobj_module(lobj_Module lobj_module) {
        this.lobj_module = lobj_module;
    }
    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }

}
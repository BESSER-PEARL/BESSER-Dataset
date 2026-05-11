




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_LuMeta extends LearningObject {

    private LocalDate creationDate;





    private lobj_Language lobj_language;




    private lobj_LearningUnit lobj_learningunit;


    public lobj_LuMeta(
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

    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }
    public lobj_LearningUnit getLobj_learningunit() {
        return lobj_learningunit;
    }

    public void setLobj_learningunit(lobj_LearningUnit lobj_learningunit) {
        this.lobj_learningunit = lobj_learningunit;
    }

}
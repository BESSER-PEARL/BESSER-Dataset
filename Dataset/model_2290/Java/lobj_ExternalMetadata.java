





import java.util.List;
import java.util.ArrayList;

public class lobj_ExternalMetadata  {

    private String file;
    private String ref;
    private String id;





    private lobj_Block lobj_block;




    private lobj_Course lobj_course;




    private lobj_LearningUnit lobj_learningunit;




    private lobj_Module lobj_module;


    public lobj_ExternalMetadata(
        String file,        String ref,        String id    ) {
        this.file = file;
        this.ref = ref;
        this.id = id;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public lobj_Block getLobj_block() {
        return lobj_block;
    }

    public void setLobj_block(lobj_Block lobj_block) {
        this.lobj_block = lobj_block;
    }
    public lobj_Course getLobj_course() {
        return lobj_course;
    }

    public void setLobj_course(lobj_Course lobj_course) {
        this.lobj_course = lobj_course;
    }
    public lobj_LearningUnit getLobj_learningunit() {
        return lobj_learningunit;
    }

    public void setLobj_learningunit(lobj_LearningUnit lobj_learningunit) {
        this.lobj_learningunit = lobj_learningunit;
    }
    public lobj_Module getLobj_module() {
        return lobj_module;
    }

    public void setLobj_module(lobj_Module lobj_module) {
        this.lobj_module = lobj_module;
    }

}
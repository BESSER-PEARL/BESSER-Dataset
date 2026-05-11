




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_BlockMeta extends LearningObject {

    private LocalDate creationDate;
    private LocalDate lastModified;
    private String rendering;
    private String lod;





    private lobj_Block lobj_block;




    private lobj_Language lobj_language;


    public lobj_BlockMeta(
        LocalDate creationDate,        LocalDate lastModified,        String rendering,        String lod    ) {
        super(
        );
        this.creationDate = creationDate;
        this.lastModified = lastModified;
        this.rendering = rendering;
        this.lod = lod;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }
    public String getRendering() {
        return rendering;
    }

    public void setRendering(String rendering) {
        this.rendering = rendering;
    }
    public String getLod() {
        return lod;
    }

    public void setLod(String lod) {
        this.lod = lod;
    }

    public lobj_Block getLobj_block() {
        return lobj_block;
    }

    public void setLobj_block(lobj_Block lobj_block) {
        this.lobj_block = lobj_block;
    }
    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }

}
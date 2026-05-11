




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_Blocktype  {

    private String name;
    private String description;
    private LocalDate creationDate;
    private String id;
    private String styleRef;





    private lobj_BlockMeta lobj_blockmeta;


    public lobj_Blocktype(
        String name,        String description,        LocalDate creationDate,        String id,        String styleRef    ) {
        this.name = name;
        this.description = description;
        this.creationDate = creationDate;
        this.id = id;
        this.styleRef = styleRef;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStyleref() {
        return styleRef;
    }

    public void setStyleref(String styleRef) {
        this.styleRef = styleRef;
    }

    public lobj_BlockMeta getLobj_blockmeta() {
        return lobj_blockmeta;
    }

    public void setLobj_blockmeta(lobj_BlockMeta lobj_blockmeta) {
        this.lobj_blockmeta = lobj_blockmeta;
    }

}
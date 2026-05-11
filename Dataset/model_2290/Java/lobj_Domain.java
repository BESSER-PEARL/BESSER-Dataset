




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_Domain  {

    private String serverURL;
    private String name;
    private String id;
    private String description;
    private LocalDate creationDate;





    private lobj_LuMeta lobj_lumeta;




    private List<lobj_Blocktype> lobj_blocktypes;




    private lobj_Blocktype lobj_blocktype;


    public lobj_Domain(
        String serverURL,        String name,        String id,        String description,        LocalDate creationDate    ) {
        this.serverURL = serverURL;
        this.name = name;
        this.id = id;
        this.description = description;
        this.creationDate = creationDate;
        this.lobj_blocktypes = new ArrayList<>();
    }

    public lobj_Domain(
        String serverURL,        String name,        String id,        String description,        LocalDate creationDate        ArrayList<lobj_Blocktype> lobj_blocktypes    ) {
        this.serverURL = serverURL;
        this.name = name;
        this.id = id;
        this.description = description;
        this.creationDate = creationDate;
        this.lobj_blocktypes = lobj_blocktypes;
    }

    public String getServerurl() {
        return serverURL;
    }

    public void setServerurl(String serverURL) {
        this.serverURL = serverURL;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    public lobj_LuMeta getLobj_lumeta() {
        return lobj_lumeta;
    }

    public void setLobj_lumeta(lobj_LuMeta lobj_lumeta) {
        this.lobj_lumeta = lobj_lumeta;
    }
    public List<lobj_Blocktype> getLobj_blocktypes() {
        return lobj_blocktypes;
    }

    public void addLobj_blocktype(Lobj_blocktype lobj_blocktype) {
        this.lobj_blocktypes.add(lobj_blocktype);
    }
    public lobj_Blocktype getLobj_blocktype() {
        return lobj_blocktype;
    }

    public void setLobj_blocktype(lobj_Blocktype lobj_blocktype) {
        this.lobj_blocktype = lobj_blocktype;
    }

}
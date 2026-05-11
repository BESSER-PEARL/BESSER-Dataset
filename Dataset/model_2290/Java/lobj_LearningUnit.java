





import java.util.List;
import java.util.ArrayList;

public class lobj_LearningUnit extends LearningObject {

    private String treeAsXml;
    private String luFile;





    private lobj_LuFolder lobj_lufolder;


    public lobj_LearningUnit(
        String treeAsXml,        String luFile    ) {
        super(
        );
        this.treeAsXml = treeAsXml;
        this.luFile = luFile;
    }


    public String getTreeasxml() {
        return treeAsXml;
    }

    public void setTreeasxml(String treeAsXml) {
        this.treeAsXml = treeAsXml;
    }
    public String getLufile() {
        return luFile;
    }

    public void setLufile(String luFile) {
        this.luFile = luFile;
    }

    public lobj_LuFolder getLobj_lufolder() {
        return lobj_lufolder;
    }

    public void setLobj_lufolder(lobj_LuFolder lobj_lufolder) {
        this.lobj_lufolder = lobj_lufolder;
    }

}
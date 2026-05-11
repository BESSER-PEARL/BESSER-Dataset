





import java.util.List;
import java.util.ArrayList;

public class lobj_Module extends LearningObject {

    private String moduleFile;
    private String treeAsXml;



    public lobj_Module(
        String moduleFile,        String treeAsXml    ) {
        super(
        );
        this.moduleFile = moduleFile;
        this.treeAsXml = treeAsXml;
    }


    public String getModulefile() {
        return moduleFile;
    }

    public void setModulefile(String moduleFile) {
        this.moduleFile = moduleFile;
    }
    public String getTreeasxml() {
        return treeAsXml;
    }

    public void setTreeasxml(String treeAsXml) {
        this.treeAsXml = treeAsXml;
    }


}
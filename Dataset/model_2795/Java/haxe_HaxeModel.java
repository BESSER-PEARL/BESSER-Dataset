





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeModel  {

    private String targetFolder;
    private String target;
    private String sourceFolder;
    private String name;



    public haxe_HaxeModel(
        String targetFolder,        String target,        String sourceFolder,        String name    ) {
        this.targetFolder = targetFolder;
        this.target = target;
        this.sourceFolder = sourceFolder;
        this.name = name;
    }


    public String getTargetfolder() {
        return targetFolder;
    }

    public void setTargetfolder(String targetFolder) {
        this.targetFolder = targetFolder;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getSourcefolder() {
        return sourceFolder;
    }

    public void setSourcefolder(String sourceFolder) {
        this.sourceFolder = sourceFolder;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
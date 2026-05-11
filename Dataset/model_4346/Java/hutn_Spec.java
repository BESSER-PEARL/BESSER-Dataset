





import java.util.List;
import java.util.ArrayList;

public class hutn_Spec  {

    private String modelFile;
    private String sourceFile;





    private List<hutn_NsUri> hutn_nsuris;




    private List<hutn_PackageObject> hutn_packageobjects;


    public hutn_Spec(
        String modelFile,        String sourceFile    ) {
        this.modelFile = modelFile;
        this.sourceFile = sourceFile;
        this.hutn_nsuris = new ArrayList<>();
        this.hutn_packageobjects = new ArrayList<>();
    }

    public hutn_Spec(
        String modelFile,        String sourceFile        ArrayList<hutn_NsUri> hutn_nsuris,        ArrayList<hutn_PackageObject> hutn_packageobjects    ) {
        this.modelFile = modelFile;
        this.sourceFile = sourceFile;
        this.hutn_nsuris = hutn_nsuris;
        this.hutn_packageobjects = hutn_packageobjects;
    }

    public String getModelfile() {
        return modelFile;
    }

    public void setModelfile(String modelFile) {
        this.modelFile = modelFile;
    }
    public String getSourcefile() {
        return sourceFile;
    }

    public void setSourcefile(String sourceFile) {
        this.sourceFile = sourceFile;
    }

    public List<hutn_NsUri> getHutn_nsuris() {
        return hutn_nsuris;
    }

    public void addHutn_nsuri(Hutn_nsuri hutn_nsuri) {
        this.hutn_nsuris.add(hutn_nsuri);
    }
    public List<hutn_PackageObject> getHutn_packageobjects() {
        return hutn_packageobjects;
    }

    public void addHutn_packageobject(Hutn_packageobject hutn_packageobject) {
        this.hutn_packageobjects.add(hutn_packageobject);
    }

}
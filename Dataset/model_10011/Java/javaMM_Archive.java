





import java.util.List;
import java.util.ArrayList;

public class javaMM_Archive extends NamedElement {

    private String originalFilePath;





    private List<javaMM_ClassFile> javamm_classfiles;




    private javaMM_Manifest javamm_manifest;


    public javaMM_Archive(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.javamm_classfiles = new ArrayList<>();
    }

    public javaMM_Archive(
        String originalFilePath        ArrayList<javaMM_ClassFile> javamm_classfiles    ) {
        this.originalFilePath = originalFilePath;
        this.javamm_classfiles = javamm_classfiles;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public List<javaMM_ClassFile> getJavamm_classfiles() {
        return javamm_classfiles;
    }

    public void addJavamm_classfile(Javamm_classfile javamm_classfile) {
        this.javamm_classfiles.add(javamm_classfile);
    }
    public javaMM_Manifest getJavamm_manifest() {
        return javamm_manifest;
    }

    public void setJavamm_manifest(javaMM_Manifest javamm_manifest) {
        this.javamm_manifest = javamm_manifest;
    }

}
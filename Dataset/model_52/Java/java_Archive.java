





import java.util.List;
import java.util.ArrayList;

public class java_Archive extends NamedElement {

    private String originalFilePath;





    private List<java_ClassFile> java_classfiles;




    private java_Manifest java_manifest;


    public java_Archive(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.java_classfiles = new ArrayList<>();
    }

    public java_Archive(
        String originalFilePath        ArrayList<java_ClassFile> java_classfiles    ) {
        this.originalFilePath = originalFilePath;
        this.java_classfiles = java_classfiles;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public List<java_ClassFile> getJava_classfiles() {
        return java_classfiles;
    }

    public void addJava_classfile(Java_classfile java_classfile) {
        this.java_classfiles.add(java_classfile);
    }
    public java_Manifest getJava_manifest() {
        return java_manifest;
    }

    public void setJava_manifest(java_Manifest java_manifest) {
        this.java_manifest = java_manifest;
    }

}
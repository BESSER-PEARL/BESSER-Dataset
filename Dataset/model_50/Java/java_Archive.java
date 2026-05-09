





import java.util.List;
import java.util.ArrayList;

public class java_Archive extends NamedElement {

    private String originalFilePath;





    private java_Manifest java_manifest;


    public java_Archive(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
    }


    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public java_Manifest getJava_manifest() {
        return java_manifest;
    }

    public void setJava_manifest(java_Manifest java_manifest) {
        this.java_manifest = java_manifest;
    }

}
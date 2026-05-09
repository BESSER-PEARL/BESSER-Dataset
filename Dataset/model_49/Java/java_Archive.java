





import java.util.List;
import java.util.ArrayList;

public class java_Archive extends NamedElement {

    private String originalFilePath;





    private java_Model java_model;


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

    public java_Model getJava_model() {
        return java_model;
    }

    public void setJava_model(java_Model java_model) {
        this.java_model = java_model;
    }

}
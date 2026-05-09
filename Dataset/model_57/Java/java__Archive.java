





import java.util.List;
import java.util.ArrayList;

public class java__Archive extends NamedElement {

    private String originalFilePath;





    private java__Model java__model;


    public java__Archive(
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

    public java__Model getJava__model() {
        return java__model;
    }

    public void setJava__model(java__Model java__model) {
        this.java__model = java__model;
    }

}
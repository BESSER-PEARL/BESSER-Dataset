





import java.util.List;
import java.util.ArrayList;

public class javaMM_Archive extends NamedElement {

    private String originalFilePath;





    private javaMM_Model javamm_model;


    public javaMM_Archive(
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

    public javaMM_Model getJavamm_model() {
        return javamm_model;
    }

    public void setJavamm_model(javaMM_Model javamm_model) {
        this.javamm_model = javamm_model;
    }

}
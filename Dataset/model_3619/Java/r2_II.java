





import java.util.List;
import java.util.ArrayList;

public class r2_II extends ANY {

    private String identifierName;
    private String extension;
    private String root;



    public r2_II(
        String identifierName,        String extension,        String root    ) {
        super(
        );
        this.identifierName = identifierName;
        this.extension = extension;
        this.root = root;
    }


    public String getIdentifiername() {
        return identifierName;
    }

    public void setIdentifiername(String identifierName) {
        this.identifierName = identifierName;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getRoot() {
        return root;
    }

    public void setRoot(String root) {
        this.root = root;
    }


}
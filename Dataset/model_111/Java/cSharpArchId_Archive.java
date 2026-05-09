





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_Archive extends NamedElement {

    private String originalFilePath;





    private cSharpArchId_Model csharparchid_model;


    public cSharpArchId_Archive(
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

    public cSharpArchId_Model getCsharparchid_model() {
        return csharparchid_model;
    }

    public void setCsharparchid_model(cSharpArchId_Model csharparchid_model) {
        this.csharparchid_model = csharparchid_model;
    }

}
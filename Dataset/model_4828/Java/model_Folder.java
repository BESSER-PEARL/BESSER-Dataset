





import java.util.List;
import java.util.ArrayList;

public class model_Folder extends FolderContainer, Documentable, Properties, ArchimateModelObject {

    private String type;





    private model_FolderContainer model_foldercontainer;


    public model_Folder(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_FolderContainer getModel_foldercontainer() {
        return model_foldercontainer;
    }

    public void setModel_foldercontainer(model_FolderContainer model_foldercontainer) {
        this.model_foldercontainer = model_foldercontainer;
    }

}
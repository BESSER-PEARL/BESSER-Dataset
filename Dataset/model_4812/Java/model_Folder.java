





import java.util.List;
import java.util.ArrayList;

public class model_Folder extends ZentaModelElement, Properties, FolderContainer, Nameable, Identifier, Documentable {






    private model_FolderContainer model_foldercontainer;


    public model_Folder(
    ) {
        super(
        );
    }



    public model_FolderContainer getModel_foldercontainer() {
        return model_foldercontainer;
    }

    public void setModel_foldercontainer(model_FolderContainer model_foldercontainer) {
        this.model_foldercontainer = model_foldercontainer;
    }

}
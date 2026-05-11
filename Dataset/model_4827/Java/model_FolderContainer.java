





import java.util.List;
import java.util.ArrayList;

public class model_FolderContainer  {






    private List<model_Folder> model_folders;


    public model_FolderContainer(
    ) {
        this.model_folders = new ArrayList<>();
    }

    public model_FolderContainer(
        ArrayList<model_Folder> model_folders    ) {
        this.model_folders = model_folders;
    }


    public List<model_Folder> getModel_folders() {
        return model_folders;
    }

    public void addModel_folder(Model_folder model_folder) {
        this.model_folders.add(model_folder);
    }

}
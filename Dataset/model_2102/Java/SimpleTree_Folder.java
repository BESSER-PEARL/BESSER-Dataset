





import java.util.List;
import java.util.ArrayList;

public class SimpleTree_Folder extends TreeElement {






    private SimpleTree_File simpletree_file;




    private List<SimpleTree_File> simpletree_files;




    private SimpleTree_Folder simpletree_folder;




    private SimpleTree_Folder simpletree_folder;


    public SimpleTree_Folder(
    ) {
        super(
        );
        this.simpletree_files = new ArrayList<>();
    }

    public SimpleTree_Folder(
        ArrayList<SimpleTree_File> simpletree_files    ) {
        this.simpletree_files = simpletree_files;
    }


    public SimpleTree_File getSimpletree_file() {
        return simpletree_file;
    }

    public void setSimpletree_file(SimpleTree_File simpletree_file) {
        this.simpletree_file = simpletree_file;
    }
    public List<SimpleTree_File> getSimpletree_files() {
        return simpletree_files;
    }

    public void addSimpletree_file(Simpletree_file simpletree_file) {
        this.simpletree_files.add(simpletree_file);
    }
    public SimpleTree_Folder getSimpletree_folder() {
        return simpletree_folder;
    }

    public void setSimpletree_folder(SimpleTree_Folder simpletree_folder) {
        this.simpletree_folder = simpletree_folder;
    }
    public SimpleTree_Folder getSimpletree_folder() {
        return simpletree_folder;
    }

    public void setSimpletree_folder(SimpleTree_Folder simpletree_folder) {
        this.simpletree_folder = simpletree_folder;
    }

}






import java.util.List;
import java.util.ArrayList;

public class MocaTree_Folder extends TreeElement {






    private MocaTree_Folder mocatree_folder;




    private List<MocaTree_Folder> mocatree_folders;


    public MocaTree_Folder(
    ) {
        super(
        );
        this.mocatree_folders = new ArrayList<>();
    }

    public MocaTree_Folder(
        ArrayList<MocaTree_Folder> mocatree_folders    ) {
        this.mocatree_folders = mocatree_folders;
    }


    public MocaTree_Folder getMocatree_folder() {
        return mocatree_folder;
    }

    public void setMocatree_folder(MocaTree_Folder mocatree_folder) {
        this.mocatree_folder = mocatree_folder;
    }
    public List<MocaTree_Folder> getMocatree_folders() {
        return mocatree_folders;
    }

    public void addMocatree_folder(Mocatree_folder mocatree_folder) {
        this.mocatree_folders.add(mocatree_folder);
    }

}
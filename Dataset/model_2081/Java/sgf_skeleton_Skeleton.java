





import java.util.List;
import java.util.ArrayList;

public class sgf_skeleton_Skeleton  {

    private String ID;





    private List<Root> roots;


    public sgf_skeleton_Skeleton(
        String ID    ) {
        this.ID = ID;
        this.roots = new ArrayList<>();
    }

    public sgf_skeleton_Skeleton(
        String ID        ArrayList<Root> roots    ) {
        this.ID = ID;
        this.roots = roots;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<Root> getRoots() {
        return roots;
    }

    public void addRoot(Root root) {
        this.roots.add(root);
    }

}
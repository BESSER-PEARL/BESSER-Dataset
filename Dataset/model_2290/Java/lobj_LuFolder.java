





import java.util.List;
import java.util.ArrayList;

public class lobj_LuFolder extends LearningObject {






    private List<lobj_LuFolder> lobj_lufolders;


    public lobj_LuFolder(
    ) {
        super(
        );
        this.lobj_lufolders = new ArrayList<>();
    }

    public lobj_LuFolder(
        ArrayList<lobj_LuFolder> lobj_lufolders    ) {
        this.lobj_lufolders = lobj_lufolders;
    }


    public List<lobj_LuFolder> getLobj_lufolders() {
        return lobj_lufolders;
    }

    public void addLobj_lufolder(Lobj_lufolder lobj_lufolder) {
        this.lobj_lufolders.add(lobj_lufolder);
    }

}
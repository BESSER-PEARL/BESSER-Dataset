





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ClassifierDefCS extends CSTNode {






    private List<TagCS> tagcss;


    public qvtoperational_cst_ClassifierDefCS(
    ) {
        super(
        );
        this.tagcss = new ArrayList<>();
    }

    public qvtoperational_cst_ClassifierDefCS(
        ArrayList<TagCS> tagcss    ) {
        this.tagcss = tagcss;
    }


    public List<TagCS> getTagcss() {
        return tagcss;
    }

    public void addTagcs(Tagcs tagcs) {
        this.tagcss.add(tagcs);
    }

}
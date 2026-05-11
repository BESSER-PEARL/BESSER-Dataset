





import java.util.List;
import java.util.ArrayList;

public class pascal_label_declaration  {






    private List<pascal_label> pascal_labels;




    private pascal_block pascal_block;


    public pascal_label_declaration(
    ) {
        this.pascal_labels = new ArrayList<>();
    }

    public pascal_label_declaration(
        ArrayList<pascal_label> pascal_labels    ) {
        this.pascal_labels = pascal_labels;
    }


    public List<pascal_label> getPascal_labels() {
        return pascal_labels;
    }

    public void addPascal_label(Pascal_label pascal_label) {
        this.pascal_labels.add(pascal_label);
    }
    public pascal_block getPascal_block() {
        return pascal_block;
    }

    public void setPascal_block(pascal_block pascal_block) {
        this.pascal_block = pascal_block;
    }

}
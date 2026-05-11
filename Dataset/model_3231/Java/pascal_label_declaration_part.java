





import java.util.List;
import java.util.ArrayList;

public class pascal_label_declaration_part  {






    private List<pascal_label> pascal_labels;




    private pascal_declaration_part pascal_declaration_part;


    public pascal_label_declaration_part(
    ) {
        this.pascal_labels = new ArrayList<>();
    }

    public pascal_label_declaration_part(
        ArrayList<pascal_label> pascal_labels    ) {
        this.pascal_labels = pascal_labels;
    }


    public List<pascal_label> getPascal_labels() {
        return pascal_labels;
    }

    public void addPascal_label(Pascal_label pascal_label) {
        this.pascal_labels.add(pascal_label);
    }
    public pascal_declaration_part getPascal_declaration_part() {
        return pascal_declaration_part;
    }

    public void setPascal_declaration_part(pascal_declaration_part pascal_declaration_part) {
        this.pascal_declaration_part = pascal_declaration_part;
    }

}
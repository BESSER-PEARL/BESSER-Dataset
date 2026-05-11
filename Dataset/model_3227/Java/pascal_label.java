





import java.util.List;
import java.util.ArrayList;

public class pascal_label extends label_declaration_part, statement {






    private pascal_label pascal_label;




    private pascal_identifier pascal_identifier;




    private pascal_gotoStatement pascal_gotostatement;


    public pascal_label(
    ) {
        super(
        );
    }



    public pascal_label getPascal_label() {
        return pascal_label;
    }

    public void setPascal_label(pascal_label pascal_label) {
        this.pascal_label = pascal_label;
    }
    public pascal_identifier getPascal_identifier() {
        return pascal_identifier;
    }

    public void setPascal_identifier(pascal_identifier pascal_identifier) {
        this.pascal_identifier = pascal_identifier;
    }
    public pascal_gotoStatement getPascal_gotostatement() {
        return pascal_gotostatement;
    }

    public void setPascal_gotostatement(pascal_gotoStatement pascal_gotostatement) {
        this.pascal_gotostatement = pascal_gotostatement;
    }

}
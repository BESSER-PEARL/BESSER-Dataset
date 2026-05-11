





import java.util.List;
import java.util.ArrayList;

public class pascal_label extends statement, goto_statement {

    private String int;





    private pascal_label_declaration_part pascal_label_declaration_part;


    public pascal_label(
        String int    ) {
        super(
        );
        this.int = int;
    }


    public String getInt() {
        return int;
    }

    public void setInt(String int) {
        this.int = int;
    }

    public pascal_label_declaration_part getPascal_label_declaration_part() {
        return pascal_label_declaration_part;
    }

    public void setPascal_label_declaration_part(pascal_label_declaration_part pascal_label_declaration_part) {
        this.pascal_label_declaration_part = pascal_label_declaration_part;
    }

}
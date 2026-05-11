





import java.util.List;
import java.util.ArrayList;

public class forms_Table extends RelationshipPageElement {






    private List<forms_Column> forms_columns;


    public forms_Table(
    ) {
        super(
        );
        this.forms_columns = new ArrayList<>();
    }

    public forms_Table(
        ArrayList<forms_Column> forms_columns    ) {
        this.forms_columns = forms_columns;
    }


    public List<forms_Column> getForms_columns() {
        return forms_columns;
    }

    public void addForms_column(Forms_column forms_column) {
        this.forms_columns.add(forms_column);
    }

}
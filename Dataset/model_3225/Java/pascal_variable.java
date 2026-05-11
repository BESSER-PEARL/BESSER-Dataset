





import java.util.List;
import java.util.ArrayList;

public class pascal_variable  {






    private pascal_actual_variable pascal_actual_variable;




    private List<pascal_identifier> pascal_identifiers;


    public pascal_variable(
    ) {
        this.pascal_identifiers = new ArrayList<>();
    }

    public pascal_variable(
        ArrayList<pascal_identifier> pascal_identifiers    ) {
        this.pascal_identifiers = pascal_identifiers;
    }


    public pascal_actual_variable getPascal_actual_variable() {
        return pascal_actual_variable;
    }

    public void setPascal_actual_variable(pascal_actual_variable pascal_actual_variable) {
        this.pascal_actual_variable = pascal_actual_variable;
    }
    public List<pascal_identifier> getPascal_identifiers() {
        return pascal_identifiers;
    }

    public void addPascal_identifier(Pascal_identifier pascal_identifier) {
        this.pascal_identifiers.add(pascal_identifier);
    }

}
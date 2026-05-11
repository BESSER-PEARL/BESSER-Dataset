





import java.util.List;
import java.util.ArrayList;

public class genericsql_Constraint  {






    private List<genericsql_Field> genericsql_fields;




    private genericsql_Table genericsql_table;


    public genericsql_Constraint(
    ) {
        this.genericsql_fields = new ArrayList<>();
    }

    public genericsql_Constraint(
        ArrayList<genericsql_Field> genericsql_fields    ) {
        this.genericsql_fields = genericsql_fields;
    }


    public List<genericsql_Field> getGenericsql_fields() {
        return genericsql_fields;
    }

    public void addGenericsql_field(Genericsql_field genericsql_field) {
        this.genericsql_fields.add(genericsql_field);
    }
    public genericsql_Table getGenericsql_table() {
        return genericsql_table;
    }

    public void setGenericsql_table(genericsql_Table genericsql_table) {
        this.genericsql_table = genericsql_table;
    }

}
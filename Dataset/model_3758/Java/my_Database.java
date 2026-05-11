





import java.util.List;
import java.util.ArrayList;

public class my_Database extends NamedElement {






    private List<my_Table> my_tables;


    public my_Database(
    ) {
        super(
        );
        this.my_tables = new ArrayList<>();
    }

    public my_Database(
        ArrayList<my_Table> my_tables    ) {
        this.my_tables = my_tables;
    }


    public List<my_Table> getMy_tables() {
        return my_tables;
    }

    public void addMy_table(My_table my_table) {
        this.my_tables.add(my_table);
    }

}
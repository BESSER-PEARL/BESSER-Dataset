





import java.util.List;
import java.util.ArrayList;

public class my_Table extends NamedElement {






    private List<my_Column> my_columns;


    public my_Table(
    ) {
        super(
        );
        this.my_columns = new ArrayList<>();
    }

    public my_Table(
        ArrayList<my_Column> my_columns    ) {
        this.my_columns = my_columns;
    }


    public List<my_Column> getMy_columns() {
        return my_columns;
    }

    public void addMy_column(My_column my_column) {
        this.my_columns.add(my_column);
    }

}






import java.util.List;
import java.util.ArrayList;

public class Row extends ColOrRowElement {






    private Table table;


    public Row(
    ) {
        super(
            boolean,            hidden,            int,            span        );
    }



    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}
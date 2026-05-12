





import java.util.List;
import java.util.ArrayList;

public class Column extends ColOrRowElement {






    private Table table;


    public Column(
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
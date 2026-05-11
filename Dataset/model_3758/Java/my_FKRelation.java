





import java.util.List;
import java.util.ArrayList;

public class my_FKRelation  {

    private String label;





    private my_Column my_column;




    private my_Database my_database;




    private my_Column my_column;


    public my_FKRelation(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public my_Column getMy_column() {
        return my_column;
    }

    public void setMy_column(my_Column my_column) {
        this.my_column = my_column;
    }
    public my_Database getMy_database() {
        return my_database;
    }

    public void setMy_database(my_Database my_database) {
        this.my_database = my_database;
    }
    public my_Column getMy_column() {
        return my_column;
    }

    public void setMy_column(my_Column my_column) {
        this.my_column = my_column;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sql4csv_Table  {

    private String name;





    private sql4csv_Query sql4csv_query;




    private sql4csv_Column sql4csv_column;




    private sql4csv_Query sql4csv_query;


    public sql4csv_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sql4csv_Query getSql4csv_query() {
        return sql4csv_query;
    }

    public void setSql4csv_query(sql4csv_Query sql4csv_query) {
        this.sql4csv_query = sql4csv_query;
    }
    public sql4csv_Column getSql4csv_column() {
        return sql4csv_column;
    }

    public void setSql4csv_column(sql4csv_Column sql4csv_column) {
        this.sql4csv_column = sql4csv_column;
    }
    public sql4csv_Query getSql4csv_query() {
        return sql4csv_query;
    }

    public void setSql4csv_query(sql4csv_Query sql4csv_query) {
        this.sql4csv_query = sql4csv_query;
    }

}
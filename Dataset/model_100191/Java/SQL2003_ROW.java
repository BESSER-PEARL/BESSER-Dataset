





import java.util.List;
import java.util.ArrayList;

public class SQL2003_ROW extends ConstructedType {






    private SQL2003_ROW sql2003_row;




    private SQL2003_ROW sql2003_row;




    private SQL2003_Field sql2003_field;




    private List<SQL2003_Field> sql2003_fields;


    public SQL2003_ROW(
    ) {
        super(
        );
        this.sql2003_fields = new ArrayList<>();
    }

    public SQL2003_ROW(
        ArrayList<SQL2003_Field> sql2003_fields    ) {
        this.sql2003_fields = sql2003_fields;
    }


    public SQL2003_ROW getSql2003_row() {
        return sql2003_row;
    }

    public void setSql2003_row(SQL2003_ROW sql2003_row) {
        this.sql2003_row = sql2003_row;
    }
    public SQL2003_ROW getSql2003_row() {
        return sql2003_row;
    }

    public void setSql2003_row(SQL2003_ROW sql2003_row) {
        this.sql2003_row = sql2003_row;
    }
    public SQL2003_Field getSql2003_field() {
        return sql2003_field;
    }

    public void setSql2003_field(SQL2003_Field sql2003_field) {
        this.sql2003_field = sql2003_field;
    }
    public List<SQL2003_Field> getSql2003_fields() {
        return sql2003_fields;
    }

    public void addSql2003_field(Sql2003_field sql2003_field) {
        this.sql2003_fields.add(sql2003_field);
    }

}






import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_ROW extends ConstructedType {






    private SQL2003_V2_ROW sql2003_v2_row;




    private SQL2003_V2_Field sql2003_v2_field;




    private List<SQL2003_V2_ROW> sql2003_v2_rows;




    private List<SQL2003_V2_Field> sql2003_v2_fields;


    public SQL2003_V2_ROW(
    ) {
        super(
        );
        this.sql2003_v2_rows = new ArrayList<>();
        this.sql2003_v2_fields = new ArrayList<>();
    }

    public SQL2003_V2_ROW(
        ArrayList<SQL2003_V2_ROW> sql2003_v2_rows,        ArrayList<SQL2003_V2_Field> sql2003_v2_fields    ) {
        this.sql2003_v2_rows = sql2003_v2_rows;
        this.sql2003_v2_fields = sql2003_v2_fields;
    }


    public SQL2003_V2_ROW getSql2003_v2_row() {
        return sql2003_v2_row;
    }

    public void setSql2003_v2_row(SQL2003_V2_ROW sql2003_v2_row) {
        this.sql2003_v2_row = sql2003_v2_row;
    }
    public SQL2003_V2_Field getSql2003_v2_field() {
        return sql2003_v2_field;
    }

    public void setSql2003_v2_field(SQL2003_V2_Field sql2003_v2_field) {
        this.sql2003_v2_field = sql2003_v2_field;
    }
    public List<SQL2003_V2_ROW> getSql2003_v2_rows() {
        return sql2003_v2_rows;
    }

    public void addSql2003_v2_row(Sql2003_v2_row sql2003_v2_row) {
        this.sql2003_v2_rows.add(sql2003_v2_row);
    }
    public List<SQL2003_V2_Field> getSql2003_v2_fields() {
        return sql2003_v2_fields;
    }

    public void addSql2003_v2_field(Sql2003_v2_field sql2003_v2_field) {
        this.sql2003_v2_fields.add(sql2003_v2_field);
    }

}
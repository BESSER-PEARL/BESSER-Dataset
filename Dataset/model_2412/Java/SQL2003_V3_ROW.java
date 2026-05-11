





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_ROW extends ConstructedType {






    private SQL2003_V3_ROW sql2003_v3_row;




    private SQL2003_V3_Field sql2003_v3_field;




    private List<SQL2003_V3_Field> sql2003_v3_fields;




    private List<SQL2003_V3_ROW> sql2003_v3_rows;


    public SQL2003_V3_ROW(
    ) {
        super(
        );
        this.sql2003_v3_fields = new ArrayList<>();
        this.sql2003_v3_rows = new ArrayList<>();
    }

    public SQL2003_V3_ROW(
        ArrayList<SQL2003_V3_Field> sql2003_v3_fields,        ArrayList<SQL2003_V3_ROW> sql2003_v3_rows    ) {
        this.sql2003_v3_fields = sql2003_v3_fields;
        this.sql2003_v3_rows = sql2003_v3_rows;
    }


    public SQL2003_V3_ROW getSql2003_v3_row() {
        return sql2003_v3_row;
    }

    public void setSql2003_v3_row(SQL2003_V3_ROW sql2003_v3_row) {
        this.sql2003_v3_row = sql2003_v3_row;
    }
    public SQL2003_V3_Field getSql2003_v3_field() {
        return sql2003_v3_field;
    }

    public void setSql2003_v3_field(SQL2003_V3_Field sql2003_v3_field) {
        this.sql2003_v3_field = sql2003_v3_field;
    }
    public List<SQL2003_V3_Field> getSql2003_v3_fields() {
        return sql2003_v3_fields;
    }

    public void addSql2003_v3_field(Sql2003_v3_field sql2003_v3_field) {
        this.sql2003_v3_fields.add(sql2003_v3_field);
    }
    public List<SQL2003_V3_ROW> getSql2003_v3_rows() {
        return sql2003_v3_rows;
    }

    public void addSql2003_v3_row(Sql2003_v3_row sql2003_v3_row) {
        this.sql2003_v3_rows.add(sql2003_v3_row);
    }

}
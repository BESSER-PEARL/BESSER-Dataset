





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_ROW extends ConstructedType {






    private SQL2003_evo_ROW sql2003_evo_row;




    private List<SQL2003_evo_Field> sql2003_evo_fields;




    private SQL2003_evo_Field sql2003_evo_field;




    private SQL2003_evo_ROW sql2003_evo_row;


    public SQL2003_evo_ROW(
    ) {
        super(
        );
        this.sql2003_evo_fields = new ArrayList<>();
    }

    public SQL2003_evo_ROW(
        ArrayList<SQL2003_evo_Field> sql2003_evo_fields    ) {
        this.sql2003_evo_fields = sql2003_evo_fields;
    }


    public SQL2003_evo_ROW getSql2003_evo_row() {
        return sql2003_evo_row;
    }

    public void setSql2003_evo_row(SQL2003_evo_ROW sql2003_evo_row) {
        this.sql2003_evo_row = sql2003_evo_row;
    }
    public List<SQL2003_evo_Field> getSql2003_evo_fields() {
        return sql2003_evo_fields;
    }

    public void addSql2003_evo_field(Sql2003_evo_field sql2003_evo_field) {
        this.sql2003_evo_fields.add(sql2003_evo_field);
    }
    public SQL2003_evo_Field getSql2003_evo_field() {
        return sql2003_evo_field;
    }

    public void setSql2003_evo_field(SQL2003_evo_Field sql2003_evo_field) {
        this.sql2003_evo_field = sql2003_evo_field;
    }
    public SQL2003_evo_ROW getSql2003_evo_row() {
        return sql2003_evo_row;
    }

    public void setSql2003_evo_row(SQL2003_evo_ROW sql2003_evo_row) {
        this.sql2003_evo_row = sql2003_evo_row;
    }

}
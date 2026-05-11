





import java.util.List;
import java.util.ArrayList;

public class SQL2003_TypedTable extends BaseTable {






    private SQL2003_StructuredType sql2003_structuredtype;




    private SQL2003_TypedTable sql2003_typedtable;




    private List<SQL2003_TypedTable> sql2003_typedtables;




    private SQL2003_StructuredType sql2003_structuredtype;


    public SQL2003_TypedTable(
    ) {
        super(
        );
        this.sql2003_typedtables = new ArrayList<>();
    }

    public SQL2003_TypedTable(
        ArrayList<SQL2003_TypedTable> sql2003_typedtables    ) {
        this.sql2003_typedtables = sql2003_typedtables;
    }


    public SQL2003_StructuredType getSql2003_structuredtype() {
        return sql2003_structuredtype;
    }

    public void setSql2003_structuredtype(SQL2003_StructuredType sql2003_structuredtype) {
        this.sql2003_structuredtype = sql2003_structuredtype;
    }
    public SQL2003_TypedTable getSql2003_typedtable() {
        return sql2003_typedtable;
    }

    public void setSql2003_typedtable(SQL2003_TypedTable sql2003_typedtable) {
        this.sql2003_typedtable = sql2003_typedtable;
    }
    public List<SQL2003_TypedTable> getSql2003_typedtables() {
        return sql2003_typedtables;
    }

    public void addSql2003_typedtable(Sql2003_typedtable sql2003_typedtable) {
        this.sql2003_typedtables.add(sql2003_typedtable);
    }
    public SQL2003_StructuredType getSql2003_structuredtype() {
        return sql2003_structuredtype;
    }

    public void setSql2003_structuredtype(SQL2003_StructuredType sql2003_structuredtype) {
        this.sql2003_structuredtype = sql2003_structuredtype;
    }

}
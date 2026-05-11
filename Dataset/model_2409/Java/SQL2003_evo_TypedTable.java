





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_TypedTable extends BaseTable {






    private SQL2003_evo_StructuredType sql2003_evo_structuredtype;




    private SQL2003_evo_TypedTable sql2003_evo_typedtable;




    private List<SQL2003_evo_TypedTable> sql2003_evo_typedtables;




    private SQL2003_evo_StructuredType sql2003_evo_structuredtype;


    public SQL2003_evo_TypedTable(
    ) {
        super(
        );
        this.sql2003_evo_typedtables = new ArrayList<>();
    }

    public SQL2003_evo_TypedTable(
        ArrayList<SQL2003_evo_TypedTable> sql2003_evo_typedtables    ) {
        this.sql2003_evo_typedtables = sql2003_evo_typedtables;
    }


    public SQL2003_evo_StructuredType getSql2003_evo_structuredtype() {
        return sql2003_evo_structuredtype;
    }

    public void setSql2003_evo_structuredtype(SQL2003_evo_StructuredType sql2003_evo_structuredtype) {
        this.sql2003_evo_structuredtype = sql2003_evo_structuredtype;
    }
    public SQL2003_evo_TypedTable getSql2003_evo_typedtable() {
        return sql2003_evo_typedtable;
    }

    public void setSql2003_evo_typedtable(SQL2003_evo_TypedTable sql2003_evo_typedtable) {
        this.sql2003_evo_typedtable = sql2003_evo_typedtable;
    }
    public List<SQL2003_evo_TypedTable> getSql2003_evo_typedtables() {
        return sql2003_evo_typedtables;
    }

    public void addSql2003_evo_typedtable(Sql2003_evo_typedtable sql2003_evo_typedtable) {
        this.sql2003_evo_typedtables.add(sql2003_evo_typedtable);
    }
    public SQL2003_evo_StructuredType getSql2003_evo_structuredtype() {
        return sql2003_evo_structuredtype;
    }

    public void setSql2003_evo_structuredtype(SQL2003_evo_StructuredType sql2003_evo_structuredtype) {
        this.sql2003_evo_structuredtype = sql2003_evo_structuredtype;
    }

}
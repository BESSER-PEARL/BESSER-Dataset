





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_TypedTable extends Table {






    private ORDB4ORA_StructuredType ordb4ora_structuredtype;




    private ORDB4ORA_StoredNestedTable ordb4ora_storednestedtable;




    private ORDB4ORA_StructuredType ordb4ora_structuredtype;




    private List<ORDB4ORA_StoredNestedTable> ordb4ora_storednestedtables;


    public ORDB4ORA_TypedTable(
    ) {
        super(
        );
        this.ordb4ora_storednestedtables = new ArrayList<>();
    }

    public ORDB4ORA_TypedTable(
        ArrayList<ORDB4ORA_StoredNestedTable> ordb4ora_storednestedtables    ) {
        this.ordb4ora_storednestedtables = ordb4ora_storednestedtables;
    }


    public ORDB4ORA_StructuredType getOrdb4ora_structuredtype() {
        return ordb4ora_structuredtype;
    }

    public void setOrdb4ora_structuredtype(ORDB4ORA_StructuredType ordb4ora_structuredtype) {
        this.ordb4ora_structuredtype = ordb4ora_structuredtype;
    }
    public ORDB4ORA_StoredNestedTable getOrdb4ora_storednestedtable() {
        return ordb4ora_storednestedtable;
    }

    public void setOrdb4ora_storednestedtable(ORDB4ORA_StoredNestedTable ordb4ora_storednestedtable) {
        this.ordb4ora_storednestedtable = ordb4ora_storednestedtable;
    }
    public ORDB4ORA_StructuredType getOrdb4ora_structuredtype() {
        return ordb4ora_structuredtype;
    }

    public void setOrdb4ora_structuredtype(ORDB4ORA_StructuredType ordb4ora_structuredtype) {
        this.ordb4ora_structuredtype = ordb4ora_structuredtype;
    }
    public List<ORDB4ORA_StoredNestedTable> getOrdb4ora_storednestedtables() {
        return ordb4ora_storednestedtables;
    }

    public void addOrdb4ora_storednestedtable(Ordb4ora_storednestedtable ordb4ora_storednestedtable) {
        this.ordb4ora_storednestedtables.add(ordb4ora_storednestedtable);
    }

}
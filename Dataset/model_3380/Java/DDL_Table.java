





import java.util.List;
import java.util.ArrayList;

public class DDL_Table extends Statement, NamedElement {






    private List<DDL_Ck> ddl_cks;




    private List<DDL_Fk> ddl_fks;




    private List<DDL_Column> ddl_columns;




    private DDL_Fk ddl_fk;




    private DDL_Pk ddl_pk;




    private List<DDL_Check> ddl_checks;


    public DDL_Table(
    ) {
        super(
        );
        this.ddl_cks = new ArrayList<>();
        this.ddl_fks = new ArrayList<>();
        this.ddl_columns = new ArrayList<>();
        this.ddl_checks = new ArrayList<>();
    }

    public DDL_Table(
        ArrayList<DDL_Ck> ddl_cks,        ArrayList<DDL_Fk> ddl_fks,        ArrayList<DDL_Column> ddl_columns,        ArrayList<DDL_Check> ddl_checks    ) {
        this.ddl_cks = ddl_cks;
        this.ddl_fks = ddl_fks;
        this.ddl_columns = ddl_columns;
        this.ddl_checks = ddl_checks;
    }


    public List<DDL_Ck> getDdl_cks() {
        return ddl_cks;
    }

    public void addDdl_ck(Ddl_ck ddl_ck) {
        this.ddl_cks.add(ddl_ck);
    }
    public List<DDL_Fk> getDdl_fks() {
        return ddl_fks;
    }

    public void addDdl_fk(Ddl_fk ddl_fk) {
        this.ddl_fks.add(ddl_fk);
    }
    public List<DDL_Column> getDdl_columns() {
        return ddl_columns;
    }

    public void addDdl_column(Ddl_column ddl_column) {
        this.ddl_columns.add(ddl_column);
    }
    public DDL_Fk getDdl_fk() {
        return ddl_fk;
    }

    public void setDdl_fk(DDL_Fk ddl_fk) {
        this.ddl_fk = ddl_fk;
    }
    public DDL_Pk getDdl_pk() {
        return ddl_pk;
    }

    public void setDdl_pk(DDL_Pk ddl_pk) {
        this.ddl_pk = ddl_pk;
    }
    public List<DDL_Check> getDdl_checks() {
        return ddl_checks;
    }

    public void addDdl_check(Ddl_check ddl_check) {
        this.ddl_checks.add(ddl_check);
    }

}
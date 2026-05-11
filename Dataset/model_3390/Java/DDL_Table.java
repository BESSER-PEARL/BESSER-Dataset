





import java.util.List;
import java.util.ArrayList;

public class DDL_Table extends NamedElement, Statement {






    private List<DDL_Check> ddl_checks;


    public DDL_Table(
    ) {
        super(
        );
        this.ddl_checks = new ArrayList<>();
    }

    public DDL_Table(
        ArrayList<DDL_Check> ddl_checks    ) {
        this.ddl_checks = ddl_checks;
    }


    public List<DDL_Check> getDdl_checks() {
        return ddl_checks;
    }

    public void addDdl_check(Ddl_check ddl_check) {
        this.ddl_checks.add(ddl_check);
    }

}
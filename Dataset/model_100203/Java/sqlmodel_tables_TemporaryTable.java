





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_tables_TemporaryTable extends BaseTable {

    private boolean deleteOnCommit;
    private boolean local;



    public sqlmodel_tables_TemporaryTable(
        boolean deleteOnCommit,        boolean local    ) {
        super(
        );
        this.deleteOnCommit = deleteOnCommit;
        this.local = local;
    }


    public boolean getDeleteoncommit() {
        return deleteOnCommit;
    }

    public void setDeleteoncommit(boolean deleteOnCommit) {
        this.deleteOnCommit = deleteOnCommit;
    }
    public boolean getLocal() {
        return local;
    }

    public void setLocal(boolean local) {
        this.local = local;
    }


}
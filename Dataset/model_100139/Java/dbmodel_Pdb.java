





import java.util.List;
import java.util.ArrayList;

public class dbmodel_Pdb  {

    private int tablePartitioning;
    private String lockSchema;
    private String name;





    private dbmodel_Class dbmodel_class;


    public dbmodel_Pdb(
        int tablePartitioning,        String lockSchema,        String name    ) {
        this.tablePartitioning = tablePartitioning;
        this.lockSchema = lockSchema;
        this.name = name;
    }


    public int getTablepartitioning() {
        return tablePartitioning;
    }

    public void setTablepartitioning(int tablePartitioning) {
        this.tablePartitioning = tablePartitioning;
    }
    public String getLockschema() {
        return lockSchema;
    }

    public void setLockschema(String lockSchema) {
        this.lockSchema = lockSchema;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbmodel_Class getDbmodel_class() {
        return dbmodel_class;
    }

    public void setDbmodel_class(dbmodel_Class dbmodel_class) {
        this.dbmodel_class = dbmodel_class;
    }

}
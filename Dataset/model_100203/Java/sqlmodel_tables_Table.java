





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_tables_Table extends SQLObject {

    private String selfRefColumnGeneration;
    private boolean updatable;
    private boolean insertable;



    public sqlmodel_tables_Table(
        String selfRefColumnGeneration,        boolean updatable,        boolean insertable    ) {
        super(
        );
        this.selfRefColumnGeneration = selfRefColumnGeneration;
        this.updatable = updatable;
        this.insertable = insertable;
    }


    public String getSelfrefcolumngeneration() {
        return selfRefColumnGeneration;
    }

    public void setSelfrefcolumngeneration(String selfRefColumnGeneration) {
        this.selfRefColumnGeneration = selfRefColumnGeneration;
    }
    public boolean getUpdatable() {
        return updatable;
    }

    public void setUpdatable(boolean updatable) {
        this.updatable = updatable;
    }
    public boolean getInsertable() {
        return insertable;
    }

    public void setInsertable(boolean insertable) {
        this.insertable = insertable;
    }


}
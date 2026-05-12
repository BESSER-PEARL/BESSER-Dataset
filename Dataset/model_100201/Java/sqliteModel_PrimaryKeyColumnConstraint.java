





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_PrimaryKeyColumnConstraint extends ColumnConstraint {

    private boolean autoincrement;
    private boolean desc;
    private boolean asc;



    public sqliteModel_PrimaryKeyColumnConstraint(
        boolean autoincrement,        boolean desc,        boolean asc    ) {
        super(
        );
        this.autoincrement = autoincrement;
        this.desc = desc;
        this.asc = asc;
    }


    public boolean getAutoincrement() {
        return autoincrement;
    }

    public void setAutoincrement(boolean autoincrement) {
        this.autoincrement = autoincrement;
    }
    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }
    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }


}
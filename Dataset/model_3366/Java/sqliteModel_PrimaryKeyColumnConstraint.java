





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_PrimaryKeyColumnConstraint extends ColumnConstraint {

    private boolean autoincrement;
    private boolean asc;
    private boolean desc;



    public sqliteModel_PrimaryKeyColumnConstraint(
        boolean autoincrement,        boolean asc,        boolean desc    ) {
        super(
        );
        this.autoincrement = autoincrement;
        this.asc = asc;
        this.desc = desc;
    }


    public boolean getAutoincrement() {
        return autoincrement;
    }

    public void setAutoincrement(boolean autoincrement) {
        this.autoincrement = autoincrement;
    }
    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }
    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }


}
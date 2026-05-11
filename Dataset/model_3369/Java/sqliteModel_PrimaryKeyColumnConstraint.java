





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_PrimaryKeyColumnConstraint extends ColumnConstraint {

    private boolean asc;
    private boolean autoincrement;
    private boolean desc;



    public sqliteModel_PrimaryKeyColumnConstraint(
        boolean asc,        boolean autoincrement,        boolean desc    ) {
        super(
        );
        this.asc = asc;
        this.autoincrement = autoincrement;
        this.desc = desc;
    }


    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
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


}
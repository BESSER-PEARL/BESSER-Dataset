





import java.util.List;
import java.util.ArrayList;

public class adb_Factor  {

    private boolean not_;
    private boolean abs;





    private adb_Primary adb_primary;




    private adb_Term adb_term;




    private adb_Primary adb_primary;


    public adb_Factor(
        boolean not_,        boolean abs    ) {
        this.not_ = not_;
        this.abs = abs;
    }


    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }
    public boolean getAbs() {
        return abs;
    }

    public void setAbs(boolean abs) {
        this.abs = abs;
    }

    public adb_Primary getAdb_primary() {
        return adb_primary;
    }

    public void setAdb_primary(adb_Primary adb_primary) {
        this.adb_primary = adb_primary;
    }
    public adb_Term getAdb_term() {
        return adb_term;
    }

    public void setAdb_term(adb_Term adb_term) {
        this.adb_term = adb_term;
    }
    public adb_Primary getAdb_primary() {
        return adb_primary;
    }

    public void setAdb_primary(adb_Primary adb_primary) {
        this.adb_primary = adb_primary;
    }

}






import java.util.List;
import java.util.ArrayList;

public class adb_Membership  {

    private boolean not_;





    private adb_Relation adb_relation;


    public adb_Membership(
        boolean not_    ) {
        this.not_ = not_;
    }


    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }

    public adb_Relation getAdb_relation() {
        return adb_relation;
    }

    public void setAdb_relation(adb_Relation adb_relation) {
        this.adb_relation = adb_relation;
    }

}
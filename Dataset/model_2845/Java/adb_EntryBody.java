





import java.util.List;
import java.util.ArrayList;

public class adb_EntryBody extends DeclarativeBlock, ProtectedOperationItem {

    private String endid;



    public adb_EntryBody(
        String endid    ) {
        super(
        );
        this.endid = endid;
    }


    public String getEndid() {
        return endid;
    }

    public void setEndid(String endid) {
        this.endid = endid;
    }


}
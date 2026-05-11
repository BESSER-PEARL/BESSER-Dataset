





import java.util.List;
import java.util.ArrayList;

public class adb_SubprogramBody extends ProperBody, DeclarativeBlock, Unit, ProtectedOperationItem {

    private String endname;



    public adb_SubprogramBody(
        String endname    ) {
        super(
        );
        this.endname = endname;
    }


    public String getEndname() {
        return endname;
    }

    public void setEndname(String endname) {
        this.endname = endname;
    }


}
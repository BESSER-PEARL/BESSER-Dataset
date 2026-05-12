





import java.util.List;
import java.util.ArrayList;

public class RelationalDBContent_DataBase extends NamedElement {

    private String SGBDname;



    public RelationalDBContent_DataBase(
        String SGBDname    ) {
        super(
        );
        this.SGBDname = SGBDname;
    }


    public String getSgbdname() {
        return SGBDname;
    }

    public void setSgbdname(String SGBDname) {
        this.SGBDname = SGBDname;
    }


}
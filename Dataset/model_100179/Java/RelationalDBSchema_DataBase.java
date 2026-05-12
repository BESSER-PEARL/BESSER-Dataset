





import java.util.List;
import java.util.ArrayList;

public class RelationalDBSchema_DataBase extends NamedElement {

    private String SGBDname;



    public RelationalDBSchema_DataBase(
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
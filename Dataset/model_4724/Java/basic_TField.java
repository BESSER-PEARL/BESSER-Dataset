





import java.util.List;
import java.util.ArrayList;

public class basic_TField extends TElementWithId {

    private String tName;



    public basic_TField(
        String tName    ) {
        super(
        );
        this.tName = tName;
    }


    public String getTname() {
        return tName;
    }

    public void setTname(String tName) {
        this.tName = tName;
    }


}
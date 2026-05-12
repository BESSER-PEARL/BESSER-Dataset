





import java.util.List;
import java.util.ArrayList;

public class BIBTEX_Entry extends LocatedElement {

    private String key;



    public BIBTEX_Entry(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}
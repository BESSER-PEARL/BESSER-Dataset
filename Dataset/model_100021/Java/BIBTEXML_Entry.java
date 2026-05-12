





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Entry  {

    private String id;
    private String abstract;



    public BIBTEXML_Entry(
        String id,        String abstract    ) {
        this.id = id;
        this.abstract = abstract;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }


}
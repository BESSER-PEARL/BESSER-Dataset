





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Entry  {

    private String abstract;
    private String id;



    public BIBTEXML_Entry(
        String abstract,        String id    ) {
        this.abstract = abstract;
        this.id = id;
    }


    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
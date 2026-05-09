





import java.util.List;
import java.util.ArrayList;

public class Docbook_RefEntryTitleType  {

    private String mixed;





    private Docbook_RefMetaType docbook_refmetatype;


    public Docbook_RefEntryTitleType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_RefMetaType getDocbook_refmetatype() {
        return docbook_refmetatype;
    }

    public void setDocbook_refmetatype(Docbook_RefMetaType docbook_refmetatype) {
        this.docbook_refmetatype = docbook_refmetatype;
    }

}
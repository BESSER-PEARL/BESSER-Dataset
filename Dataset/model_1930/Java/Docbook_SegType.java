





import java.util.List;
import java.util.ArrayList;

public class Docbook_SegType  {

    private String group;
    private String errorcode;
    private String mixed;
    private String errortext;





    private Docbook_SegListItemType docbook_seglistitemtype;


    public Docbook_SegType(
        String group,        String errorcode,        String mixed,        String errortext    ) {
        this.group = group;
        this.errorcode = errorcode;
        this.mixed = mixed;
        this.errortext = errortext;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getErrorcode() {
        return errorcode;
    }

    public void setErrorcode(String errorcode) {
        this.errorcode = errorcode;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getErrortext() {
        return errortext;
    }

    public void setErrortext(String errortext) {
        this.errortext = errortext;
    }

    public Docbook_SegListItemType getDocbook_seglistitemtype() {
        return docbook_seglistitemtype;
    }

    public void setDocbook_seglistitemtype(Docbook_SegListItemType docbook_seglistitemtype) {
        this.docbook_seglistitemtype = docbook_seglistitemtype;
    }

}
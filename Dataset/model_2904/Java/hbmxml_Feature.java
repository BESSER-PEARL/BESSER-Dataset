





import java.util.List;
import java.util.ArrayList;

public class hbmxml_Feature extends NamedElement {

    private String kind;





    private hbmxml_Type hbmxml_type;


    public hbmxml_Feature(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public hbmxml_Type getHbmxml_type() {
        return hbmxml_type;
    }

    public void setHbmxml_type(hbmxml_Type hbmxml_type) {
        this.hbmxml_type = hbmxml_type;
    }

}
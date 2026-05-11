





import java.util.List;
import java.util.ArrayList;

public class bombXML_Feature extends NamedElement {

    private String kind;





    private bombXML_Type bombxml_type;


    public bombXML_Feature(
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

    public bombXML_Type getBombxml_type() {
        return bombxml_type;
    }

    public void setBombxml_type(bombXML_Type bombxml_type) {
        this.bombxml_type = bombxml_type;
    }

}
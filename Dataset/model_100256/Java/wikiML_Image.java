





import java.util.List;
import java.util.ArrayList;

public class wikiML_Image extends ParagraphTypes {

    private String hAlign;
    private String type;
    private String name;



    public wikiML_Image(
        String hAlign,        String type,        String name    ) {
        super(
        );
        this.hAlign = hAlign;
        this.type = type;
        this.name = name;
    }


    public String getHalign() {
        return hAlign;
    }

    public void setHalign(String hAlign) {
        this.hAlign = hAlign;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}






import java.util.List;
import java.util.ArrayList;

public class wikiML_Image extends ParagraphTypes {

    private String hAlign;
    private String name;
    private String type;



    public wikiML_Image(
        String hAlign,        String name,        String type    ) {
        super(
        );
        this.hAlign = hAlign;
        this.name = name;
        this.type = type;
    }


    public String getHalign() {
        return hAlign;
    }

    public void setHalign(String hAlign) {
        this.hAlign = hAlign;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
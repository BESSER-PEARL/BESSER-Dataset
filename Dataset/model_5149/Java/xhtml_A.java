





import java.util.List;
import java.util.ArrayList;

public class xhtml_A extends AContent {

    private String lang;
    private String class_;
    private String shape;
    private String href;
    private String coords;
    private String style;
    private String type;
    private String name;



    public xhtml_A(
        String lang,        String class_,        String shape,        String href,        String coords,        String style,        String type,        String name    ) {
        super(
        );
        this.lang = lang;
        this.class_ = class_;
        this.shape = shape;
        this.href = href;
        this.coords = coords;
        this.style = style;
        this.type = type;
        this.name = name;
    }


    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getCoords() {
        return coords;
    }

    public void setCoords(String coords) {
        this.coords = coords;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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
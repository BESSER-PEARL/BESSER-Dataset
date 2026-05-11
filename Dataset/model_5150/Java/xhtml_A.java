





import java.util.List;
import java.util.ArrayList;

public class xhtml_A extends AContent {

    private String class_;
    private String href;
    private String style;
    private String lang;
    private String coords;
    private String type;
    private String shape;
    private String name;



    public xhtml_A(
        String class_,        String href,        String style,        String lang,        String coords,        String type,        String shape,        String name    ) {
        super(
        );
        this.class_ = class_;
        this.href = href;
        this.style = style;
        this.lang = lang;
        this.coords = coords;
        this.type = type;
        this.shape = shape;
        this.name = name;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getCoords() {
        return coords;
    }

    public void setCoords(String coords) {
        this.coords = coords;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
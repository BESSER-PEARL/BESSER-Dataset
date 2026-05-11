





import java.util.List;
import java.util.ArrayList;

public class xhtml_AType extends AContent {

    private String type;
    private String shape;
    private String href;
    private String charset;
    private String hreflang;
    private String rel;
    private String class_;
    private String name;
    private String title;
    private String coords;
    private String style;
    private String rev;
    private String id;





    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_AType(
        String type,        String shape,        String href,        String charset,        String hreflang,        String rel,        String class_,        String name,        String title,        String coords,        String style,        String rev,        String id    ) {
        super(
        );
        this.type = type;
        this.shape = shape;
        this.href = href;
        this.charset = charset;
        this.hreflang = hreflang;
        this.rel = rel;
        this.class_ = class_;
        this.name = name;
        this.title = title;
        this.coords = coords;
        this.style = style;
        this.rev = rev;
        this.id = id;
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
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getCharset() {
        return charset;
    }

    public void setCharset(String charset) {
        this.charset = charset;
    }
    public String getHreflang() {
        return hreflang;
    }

    public void setHreflang(String hreflang) {
        this.hreflang = hreflang;
    }
    public String getRel() {
        return rel;
    }

    public void setRel(String rel) {
        this.rel = rel;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public String getRev() {
        return rev;
    }

    public void setRev(String rev) {
        this.rev = rev;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }

}
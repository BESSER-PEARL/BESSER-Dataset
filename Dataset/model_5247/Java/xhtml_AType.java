





import java.util.List;
import java.util.ArrayList;

public class xhtml_AType extends AContent {

    private String type;
    private String class_;
    private String shape;
    private String style;
    private String rel;
    private String name;
    private String id;
    private String charset;
    private String href;
    private String coords;
    private String rev;
    private String title;
    private String hreflang;





    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_AType(
        String type,        String class_,        String shape,        String style,        String rel,        String name,        String id,        String charset,        String href,        String coords,        String rev,        String title,        String hreflang    ) {
        super(
        );
        this.type = type;
        this.class_ = class_;
        this.shape = shape;
        this.style = style;
        this.rel = rel;
        this.name = name;
        this.id = id;
        this.charset = charset;
        this.href = href;
        this.coords = coords;
        this.rev = rev;
        this.title = title;
        this.hreflang = hreflang;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getRel() {
        return rel;
    }

    public void setRel(String rel) {
        this.rel = rel;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCharset() {
        return charset;
    }

    public void setCharset(String charset) {
        this.charset = charset;
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
    public String getRev() {
        return rev;
    }

    public void setRev(String rev) {
        this.rev = rev;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getHreflang() {
        return hreflang;
    }

    public void setHreflang(String hreflang) {
        this.hreflang = hreflang;
    }

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }

}
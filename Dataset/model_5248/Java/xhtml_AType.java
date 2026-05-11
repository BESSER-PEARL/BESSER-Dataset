





import java.util.List;
import java.util.ArrayList;

public class xhtml_AType extends AContent {

    private String name;
    private String style;
    private String class_;
    private String id;
    private String rel;
    private String hreflang;
    private String shape;
    private String type;
    private String charset;
    private String href;
    private String title;
    private String rev;
    private String coords;





    private xhtml_Flow xhtml_flow;




    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_Inline xhtml_inline;




    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_PreContent xhtml_precontent;


    public xhtml_AType(
        String name,        String style,        String class_,        String id,        String rel,        String hreflang,        String shape,        String type,        String charset,        String href,        String title,        String rev,        String coords    ) {
        super(
        );
        this.name = name;
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.rel = rel;
        this.hreflang = hreflang;
        this.shape = shape;
        this.type = type;
        this.charset = charset;
        this.href = href;
        this.title = title;
        this.rev = rev;
        this.coords = coords;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getRel() {
        return rel;
    }

    public void setRel(String rel) {
        this.rel = rel;
    }
    public String getHreflang() {
        return hreflang;
    }

    public void setHreflang(String hreflang) {
        this.hreflang = hreflang;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getRev() {
        return rev;
    }

    public void setRev(String rev) {
        this.rev = rev;
    }
    public String getCoords() {
        return coords;
    }

    public void setCoords(String coords) {
        this.coords = coords;
    }

    public xhtml_Flow getXhtml_flow() {
        return xhtml_flow;
    }

    public void setXhtml_flow(xhtml_Flow xhtml_flow) {
        this.xhtml_flow = xhtml_flow;
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_Inline getXhtml_inline() {
        return xhtml_inline;
    }

    public void setXhtml_inline(xhtml_Inline xhtml_inline) {
        this.xhtml_inline = xhtml_inline;
    }
    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_PreContent getXhtml_precontent() {
        return xhtml_precontent;
    }

    public void setXhtml_precontent(xhtml_PreContent xhtml_precontent) {
        this.xhtml_precontent = xhtml_precontent;
    }

}






import java.util.List;
import java.util.ArrayList;

public class xhtml_ColType  {

    private String valign;
    private String lang;
    private String span;
    private String width;
    private String title;
    private String align;
    private String dir;
    private String char;
    private String class_;
    private String id;
    private String style;
    private String lang1;
    private String charoff;





    private xhtml_ColgroupType xhtml_colgrouptype;




    private xhtml_TableType xhtml_tabletype;


    public xhtml_ColType(
        String valign,        String lang,        String span,        String width,        String title,        String align,        String dir,        String char,        String class_,        String id,        String style,        String lang1,        String charoff    ) {
        this.valign = valign;
        this.lang = lang;
        this.span = span;
        this.width = width;
        this.title = title;
        this.align = align;
        this.dir = dir;
        this.char = char;
        this.class_ = class_;
        this.id = id;
        this.style = style;
        this.lang1 = lang1;
        this.charoff = charoff;
    }


    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }

    public xhtml_ColgroupType getXhtml_colgrouptype() {
        return xhtml_colgrouptype;
    }

    public void setXhtml_colgrouptype(xhtml_ColgroupType xhtml_colgrouptype) {
        this.xhtml_colgrouptype = xhtml_colgrouptype;
    }
    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }

}






import java.util.List;
import java.util.ArrayList;

public class xhtml_TfootType  {

    private String valign;
    private String dir;
    private String align;
    private String lang1;
    private String char;
    private String lang;
    private String title;
    private String id;
    private String charoff;
    private String class_;
    private String style;





    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_TableType xhtml_tabletype;


    public xhtml_TfootType(
        String valign,        String dir,        String align,        String lang1,        String char,        String lang,        String title,        String id,        String charoff,        String class_,        String style    ) {
        this.valign = valign;
        this.dir = dir;
        this.align = align;
        this.lang1 = lang1;
        this.char = char;
        this.lang = lang;
        this.title = title;
        this.id = id;
        this.charoff = charoff;
        this.class_ = class_;
        this.style = style;
    }


    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }

}
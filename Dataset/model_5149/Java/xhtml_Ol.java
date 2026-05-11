





import java.util.List;
import java.util.ArrayList;

public class xhtml_Ol  {

    private String li;
    private String class_;
    private String style;
    private String lang;





    private xhtml_Block xhtml_block;




    private xhtml_Object xhtml_object;


    public xhtml_Ol(
        String li,        String class_,        String style,        String lang    ) {
        this.li = li;
        this.class_ = class_;
        this.style = style;
        this.lang = lang;
    }


    public String getLi() {
        return li;
    }

    public void setLi(String li) {
        this.li = li;
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
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }

    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public xhtml_Object getXhtml_object() {
        return xhtml_object;
    }

    public void setXhtml_object(xhtml_Object xhtml_object) {
        this.xhtml_object = xhtml_object;
    }

}
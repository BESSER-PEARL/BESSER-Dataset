





import java.util.List;
import java.util.ArrayList;

public class xhtml_Pre extends PreContent {

    private String style;
    private String lang;
    private String class_;
    private String space;





    private xhtml_Object xhtml_object;




    private xhtml_Block xhtml_block;


    public xhtml_Pre(
        String style,        String lang,        String class_,        String space    ) {
        super(
        );
        this.style = style;
        this.lang = lang;
        this.class_ = class_;
        this.space = space;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getSpace() {
        return space;
    }

    public void setSpace(String space) {
        this.space = space;
    }

    public xhtml_Object getXhtml_object() {
        return xhtml_object;
    }

    public void setXhtml_object(xhtml_Object xhtml_object) {
        this.xhtml_object = xhtml_object;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }

}
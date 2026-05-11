





import java.util.List;
import java.util.ArrayList;

public class xhtml_Dl  {

    private String lang;
    private String group;
    private String class_;
    private String style;





    private xhtml_Object xhtml_object;




    private List<xhtml_Dt> xhtml_dts;




    private xhtml_Block xhtml_block;


    public xhtml_Dl(
        String lang,        String group,        String class_,        String style    ) {
        this.lang = lang;
        this.group = group;
        this.class_ = class_;
        this.style = style;
        this.xhtml_dts = new ArrayList<>();
    }

    public xhtml_Dl(
        String lang,        String group,        String class_,        String style        ArrayList<xhtml_Dt> xhtml_dts    ) {
        this.lang = lang;
        this.group = group;
        this.class_ = class_;
        this.style = style;
        this.xhtml_dts = xhtml_dts;
    }

    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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

    public xhtml_Object getXhtml_object() {
        return xhtml_object;
    }

    public void setXhtml_object(xhtml_Object xhtml_object) {
        this.xhtml_object = xhtml_object;
    }
    public List<xhtml_Dt> getXhtml_dts() {
        return xhtml_dts;
    }

    public void addXhtml_dt(Xhtml_dt xhtml_dt) {
        this.xhtml_dts.add(xhtml_dt);
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dg_StyleSelector  {

    private String kind;
    private String class_;





    private dg_StyleRule dg_stylerule;


    public dg_StyleSelector(
        String kind,        String class_    ) {
        this.kind = kind;
        this.class_ = class_;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public dg_StyleRule getDg_stylerule() {
        return dg_stylerule;
    }

    public void setDg_stylerule(dg_StyleRule dg_stylerule) {
        this.dg_stylerule = dg_stylerule;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dg_GraphicalElement extends Definition {

    private String layoutData;
    private String class_;





    private dg_ClipPath dg_clippath;




    private dg_Group dg_group;




    private dg_Group dg_group;




    private dg_Use dg_use;


    public dg_GraphicalElement(
        String layoutData,        String class_    ) {
        super(
        );
        this.layoutData = layoutData;
        this.class_ = class_;
    }


    public String getLayoutdata() {
        return layoutData;
    }

    public void setLayoutdata(String layoutData) {
        this.layoutData = layoutData;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public dg_ClipPath getDg_clippath() {
        return dg_clippath;
    }

    public void setDg_clippath(dg_ClipPath dg_clippath) {
        this.dg_clippath = dg_clippath;
    }
    public dg_Group getDg_group() {
        return dg_group;
    }

    public void setDg_group(dg_Group dg_group) {
        this.dg_group = dg_group;
    }
    public dg_Group getDg_group() {
        return dg_group;
    }

    public void setDg_group(dg_Group dg_group) {
        this.dg_group = dg_group;
    }
    public dg_Use getDg_use() {
        return dg_use;
    }

    public void setDg_use(dg_Use dg_use) {
        this.dg_use = dg_use;
    }

}






import java.util.List;
import java.util.ArrayList;

public class gv_AttributeList extends Commentable {






    private gv_AttributeStatement gv_attributestatement;




    private gv_AttributeList gv_attributelist;




    private gv_Attributable gv_attributable;


    public gv_AttributeList(
    ) {
        super(
        );
    }



    public gv_AttributeStatement getGv_attributestatement() {
        return gv_attributestatement;
    }

    public void setGv_attributestatement(gv_AttributeStatement gv_attributestatement) {
        this.gv_attributestatement = gv_attributestatement;
    }
    public gv_AttributeList getGv_attributelist() {
        return gv_attributelist;
    }

    public void setGv_attributelist(gv_AttributeList gv_attributelist) {
        this.gv_attributelist = gv_attributelist;
    }
    public gv_Attributable getGv_attributable() {
        return gv_attributable;
    }

    public void setGv_attributable(gv_Attributable gv_attributable) {
        this.gv_attributable = gv_attributable;
    }

}






import java.util.List;
import java.util.ArrayList;

public class cs_CSTemplateDescription extends CSNode {

    private float scale;





    private cs_CSElement cs_cselement;


    public cs_CSTemplateDescription(
        float scale    ) {
        super(
        );
        this.scale = scale;
    }


    public float getScale() {
        return scale;
    }

    public void setScale(float scale) {
        this.scale = scale;
    }

    public cs_CSElement getCs_cselement() {
        return cs_cselement;
    }

    public void setCs_cselement(cs_CSElement cs_cselement) {
        this.cs_cselement = cs_cselement;
    }

}
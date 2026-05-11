





import java.util.List;
import java.util.ArrayList;

public class coCoMM_OptimizationDR extends DecisionRule {

    private String funct;





    private coCoMM_AttributeType cocomm_attributetype;


    public coCoMM_OptimizationDR(
        String funct    ) {
        super(
        );
        this.funct = funct;
    }


    public String getFunct() {
        return funct;
    }

    public void setFunct(String funct) {
        this.funct = funct;
    }

    public coCoMM_AttributeType getCocomm_attributetype() {
        return cocomm_attributetype;
    }

    public void setCocomm_attributetype(coCoMM_AttributeType cocomm_attributetype) {
        this.cocomm_attributetype = cocomm_attributetype;
    }

}
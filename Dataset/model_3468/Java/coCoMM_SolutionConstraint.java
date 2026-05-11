





import java.util.List;
import java.util.ArrayList;

public class coCoMM_SolutionConstraint  {

    private String type;





    private coCoMM_CoCo cocomm_coco;


    public coCoMM_SolutionConstraint(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public coCoMM_CoCo getCocomm_coco() {
        return cocomm_coco;
    }

    public void setCocomm_coco(coCoMM_CoCo cocomm_coco) {
        this.cocomm_coco = cocomm_coco;
    }

}
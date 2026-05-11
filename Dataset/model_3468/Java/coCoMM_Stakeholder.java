





import java.util.List;
import java.util.ArrayList;

public class coCoMM_Stakeholder  {

    private String name;
    private String job;





    private coCoMM_CoCo cocomm_coco;


    public coCoMM_Stakeholder(
        String name,        String job    ) {
        this.name = name;
        this.job = job;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public coCoMM_CoCo getCocomm_coco() {
        return cocomm_coco;
    }

    public void setCocomm_coco(coCoMM_CoCo cocomm_coco) {
        this.cocomm_coco = cocomm_coco;
    }

}
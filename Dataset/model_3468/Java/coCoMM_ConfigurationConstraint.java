





import java.util.List;
import java.util.ArrayList;

public class coCoMM_ConfigurationConstraint  {

    private String id;
    private String name;
    private String type;





    private coCoMM_CoCo cocomm_coco;


    public coCoMM_ConfigurationConstraint(
        String id,        String name,        String type    ) {
        this.id = id;
        this.name = name;
        this.type = type;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
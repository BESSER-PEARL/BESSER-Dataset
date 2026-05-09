





import java.util.List;
import java.util.ArrayList;

public class eTJ_Task extends Property {

    private String name;
    private String id;





    private eTJ_SupplementTask etj_supplementtask;


    public eTJ_Task(
        String name,        String id    ) {
        super(
        );
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public eTJ_SupplementTask getEtj_supplementtask() {
        return etj_supplementtask;
    }

    public void setEtj_supplementtask(eTJ_SupplementTask etj_supplementtask) {
        this.etj_supplementtask = etj_supplementtask;
    }

}
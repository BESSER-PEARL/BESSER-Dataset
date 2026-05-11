





import java.util.List;
import java.util.ArrayList;

public class entitymm_Entity extends Type {

    private boolean isPersistent;
    private int size;
    private String desc;





    private List<entitymm_Attribute> entitymm_attributes;




    private entitymm_Attribute entitymm_attribute;


    public entitymm_Entity(
        boolean isPersistent,        int size,        String desc    ) {
        super(
        );
        this.isPersistent = isPersistent;
        this.size = size;
        this.desc = desc;
        this.entitymm_attributes = new ArrayList<>();
    }

    public entitymm_Entity(
        boolean isPersistent,        int size,        String desc        ArrayList<entitymm_Attribute> entitymm_attributes    ) {
        this.isPersistent = isPersistent;
        this.size = size;
        this.desc = desc;
        this.entitymm_attributes = entitymm_attributes;
    }

    public boolean getIspersistent() {
        return isPersistent;
    }

    public void setIspersistent(boolean isPersistent) {
        this.isPersistent = isPersistent;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public List<entitymm_Attribute> getEntitymm_attributes() {
        return entitymm_attributes;
    }

    public void addEntitymm_attribute(Entitymm_attribute entitymm_attribute) {
        this.entitymm_attributes.add(entitymm_attribute);
    }
    public entitymm_Attribute getEntitymm_attribute() {
        return entitymm_attribute;
    }

    public void setEntitymm_attribute(entitymm_Attribute entitymm_attribute) {
        this.entitymm_attribute = entitymm_attribute;
    }

}
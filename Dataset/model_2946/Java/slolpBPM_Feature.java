





import java.util.List;
import java.util.ArrayList;

public class slolpBPM_Feature  {

    private boolean many;
    private String name;





    private slolpBPM_Type slolpbpm_type;




    private slolpBPM_Entity slolpbpm_entity;


    public slolpBPM_Feature(
        boolean many,        String name    ) {
        this.many = many;
        this.name = name;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public slolpBPM_Type getSlolpbpm_type() {
        return slolpbpm_type;
    }

    public void setSlolpbpm_type(slolpBPM_Type slolpbpm_type) {
        this.slolpbpm_type = slolpbpm_type;
    }
    public slolpBPM_Entity getSlolpbpm_entity() {
        return slolpbpm_entity;
    }

    public void setSlolpbpm_entity(slolpBPM_Entity slolpbpm_entity) {
        this.slolpbpm_entity = slolpbpm_entity;
    }

}
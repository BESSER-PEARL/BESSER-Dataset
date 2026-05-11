





import java.util.List;
import java.util.ArrayList;

public class ER_ERAttribute extends ERElem {

    private boolean isKey;
    private String name;





    private ER_Entity er_entity;




    private ER_Relship er_relship;




    private ER_Relship er_relship;




    private ER_Entity er_entity;


    public ER_ERAttribute(
        boolean isKey,        String name    ) {
        super(
        );
        this.isKey = isKey;
        this.name = name;
    }


    public boolean getIskey() {
        return isKey;
    }

    public void setIskey(boolean isKey) {
        this.isKey = isKey;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ER_Entity getEr_entity() {
        return er_entity;
    }

    public void setEr_entity(ER_Entity er_entity) {
        this.er_entity = er_entity;
    }
    public ER_Relship getEr_relship() {
        return er_relship;
    }

    public void setEr_relship(ER_Relship er_relship) {
        this.er_relship = er_relship;
    }
    public ER_Relship getEr_relship() {
        return er_relship;
    }

    public void setEr_relship(ER_Relship er_relship) {
        this.er_relship = er_relship;
    }
    public ER_Entity getEr_entity() {
        return er_entity;
    }

    public void setEr_entity(ER_Entity er_entity) {
        this.er_entity = er_entity;
    }

}
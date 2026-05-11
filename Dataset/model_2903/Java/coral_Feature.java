





import java.util.List;
import java.util.ArrayList;

public class coral_Feature extends NamedElement {

    private String kind;





    private coral_Entity coral_entity;


    public coral_Feature(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public coral_Entity getCoral_entity() {
        return coral_entity;
    }

    public void setCoral_entity(coral_Entity coral_entity) {
        this.coral_entity = coral_entity;
    }

}
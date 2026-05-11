





import java.util.List;
import java.util.ArrayList;

public class myDsl_IsServer  {

    private String value;





    private myDsl_Entity mydsl_entity;


    public myDsl_IsServer(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public myDsl_Entity getMydsl_entity() {
        return mydsl_entity;
    }

    public void setMydsl_entity(myDsl_Entity mydsl_entity) {
        this.mydsl_entity = mydsl_entity;
    }

}
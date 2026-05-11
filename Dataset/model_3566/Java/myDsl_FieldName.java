





import java.util.List;
import java.util.ArrayList;

public class myDsl_FieldName  {

    private String id;





    private myDsl_Key mydsl_key;


    public myDsl_FieldName(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_Key getMydsl_key() {
        return mydsl_key;
    }

    public void setMydsl_key(myDsl_Key mydsl_key) {
        this.mydsl_key = mydsl_key;
    }

}






import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeName  {

    private String id;





    private myDsl_Type mydsl_type;


    public myDsl_TypeName(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}
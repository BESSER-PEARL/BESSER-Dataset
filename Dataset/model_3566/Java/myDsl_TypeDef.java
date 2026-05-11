





import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeDef  {

    private String id;





    private myDsl_TypeSpec mydsl_typespec;




    private myDsl_Type mydsl_type;


    public myDsl_TypeDef(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_TypeSpec getMydsl_typespec() {
        return mydsl_typespec;
    }

    public void setMydsl_typespec(myDsl_TypeSpec mydsl_typespec) {
        this.mydsl_typespec = mydsl_typespec;
    }
    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}






import java.util.List;
import java.util.ArrayList;

public class myDsl_StructType  {

    private String struct;





    private myDsl_TypeLit mydsl_typelit;


    public myDsl_StructType(
        String struct    ) {
        this.struct = struct;
    }


    public String getStruct() {
        return struct;
    }

    public void setStruct(String struct) {
        this.struct = struct;
    }

    public myDsl_TypeLit getMydsl_typelit() {
        return mydsl_typelit;
    }

    public void setMydsl_typelit(myDsl_TypeLit mydsl_typelit) {
        this.mydsl_typelit = mydsl_typelit;
    }

}
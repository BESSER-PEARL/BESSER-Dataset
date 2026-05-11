





import java.util.List;
import java.util.ArrayList;

public class myDsl_BaseType  {






    private myDsl_Type mydsl_type;




    private myDsl_PointerType mydsl_pointertype;


    public myDsl_BaseType(
    ) {
    }



    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }
    public myDsl_PointerType getMydsl_pointertype() {
        return mydsl_pointertype;
    }

    public void setMydsl_pointertype(myDsl_PointerType mydsl_pointertype) {
        this.mydsl_pointertype = mydsl_pointertype;
    }

}
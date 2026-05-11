





import java.util.List;
import java.util.ArrayList;

public class myDsl_atomic_type_specifier  {

    private String atomic;





    private myDsl_type_specifier mydsl_type_specifier;




    private myDsl_type_name mydsl_type_name;


    public myDsl_atomic_type_specifier(
        String atomic    ) {
        this.atomic = atomic;
    }


    public String getAtomic() {
        return atomic;
    }

    public void setAtomic(String atomic) {
        this.atomic = atomic;
    }

    public myDsl_type_specifier getMydsl_type_specifier() {
        return mydsl_type_specifier;
    }

    public void setMydsl_type_specifier(myDsl_type_specifier mydsl_type_specifier) {
        this.mydsl_type_specifier = mydsl_type_specifier;
    }
    public myDsl_type_name getMydsl_type_name() {
        return mydsl_type_name;
    }

    public void setMydsl_type_name(myDsl_type_name mydsl_type_name) {
        this.mydsl_type_name = mydsl_type_name;
    }

}
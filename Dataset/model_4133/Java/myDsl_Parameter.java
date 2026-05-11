





import java.util.List;
import java.util.ArrayList;

public class myDsl_Parameter  {

    private String name;





    private myDsl_Method mydsl_method;


    public myDsl_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Method getMydsl_method() {
        return mydsl_method;
    }

    public void setMydsl_method(myDsl_Method mydsl_method) {
        this.mydsl_method = mydsl_method;
    }

}
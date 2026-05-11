





import java.util.List;
import java.util.ArrayList;

public class myDsl_MethodName  {

    private String id;





    private myDsl_MethodSpec mydsl_methodspec;


    public myDsl_MethodName(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_MethodSpec getMydsl_methodspec() {
        return mydsl_methodspec;
    }

    public void setMydsl_methodspec(myDsl_MethodSpec mydsl_methodspec) {
        this.mydsl_methodspec = mydsl_methodspec;
    }

}
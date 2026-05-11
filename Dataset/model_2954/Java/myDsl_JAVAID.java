





import java.util.List;
import java.util.ArrayList;

public class myDsl_JAVAID  {

    private String name;





    private myDsl_TypeDef mydsl_typedef;


    public myDsl_JAVAID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_TypeDef getMydsl_typedef() {
        return mydsl_typedef;
    }

    public void setMydsl_typedef(myDsl_TypeDef mydsl_typedef) {
        this.mydsl_typedef = mydsl_typedef;
    }

}
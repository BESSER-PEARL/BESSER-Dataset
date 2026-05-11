





import java.util.List;
import java.util.ArrayList;

public class myDsl_MapType  {

    private String map;





    private myDsl_TypeLit mydsl_typelit;


    public myDsl_MapType(
        String map    ) {
        this.map = map;
    }


    public String getMap() {
        return map;
    }

    public void setMap(String map) {
        this.map = map;
    }

    public myDsl_TypeLit getMydsl_typelit() {
        return mydsl_typelit;
    }

    public void setMydsl_typelit(myDsl_TypeLit mydsl_typelit) {
        this.mydsl_typelit = mydsl_typelit;
    }

}
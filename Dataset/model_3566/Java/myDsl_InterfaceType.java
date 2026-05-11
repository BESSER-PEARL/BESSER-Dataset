





import java.util.List;
import java.util.ArrayList;

public class myDsl_InterfaceType  {

    private String interface;





    private myDsl_TypeLit mydsl_typelit;


    public myDsl_InterfaceType(
        String interface    ) {
        this.interface = interface;
    }


    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }

    public myDsl_TypeLit getMydsl_typelit() {
        return mydsl_typelit;
    }

    public void setMydsl_typelit(myDsl_TypeLit mydsl_typelit) {
        this.mydsl_typelit = mydsl_typelit;
    }

}
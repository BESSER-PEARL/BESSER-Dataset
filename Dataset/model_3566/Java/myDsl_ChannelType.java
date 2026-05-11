





import java.util.List;
import java.util.ArrayList;

public class myDsl_ChannelType  {

    private String chan;





    private myDsl_TypeLit mydsl_typelit;




    private myDsl_ElementType mydsl_elementtype;


    public myDsl_ChannelType(
        String chan    ) {
        this.chan = chan;
    }


    public String getChan() {
        return chan;
    }

    public void setChan(String chan) {
        this.chan = chan;
    }

    public myDsl_TypeLit getMydsl_typelit() {
        return mydsl_typelit;
    }

    public void setMydsl_typelit(myDsl_TypeLit mydsl_typelit) {
        this.mydsl_typelit = mydsl_typelit;
    }
    public myDsl_ElementType getMydsl_elementtype() {
        return mydsl_elementtype;
    }

    public void setMydsl_elementtype(myDsl_ElementType mydsl_elementtype) {
        this.mydsl_elementtype = mydsl_elementtype;
    }

}






import java.util.List;
import java.util.ArrayList;

public class langage_while_SYMB  {

    private String bs;
    private String cf;





    private langage_while_Function langage_while_function;


    public langage_while_SYMB(
        String bs,        String cf    ) {
        this.bs = bs;
        this.cf = cf;
    }


    public String getBs() {
        return bs;
    }

    public void setBs(String bs) {
        this.bs = bs;
    }
    public String getCf() {
        return cf;
    }

    public void setCf(String cf) {
        this.cf = cf;
    }

    public langage_while_Function getLangage_while_function() {
        return langage_while_function;
    }

    public void setLangage_while_function(langage_while_Function langage_while_function) {
        this.langage_while_function = langage_while_function;
    }

}
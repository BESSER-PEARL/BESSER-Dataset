





import java.util.List;
import java.util.ArrayList;

public class langage_while_VAR  {

    private String cf;
    private String bv;





    private langage_while_Vars langage_while_vars;




    private langage_while_Input langage_while_input;




    private langage_while_Output langage_while_output;


    public langage_while_VAR(
        String cf,        String bv    ) {
        this.cf = cf;
        this.bv = bv;
    }


    public String getCf() {
        return cf;
    }

    public void setCf(String cf) {
        this.cf = cf;
    }
    public String getBv() {
        return bv;
    }

    public void setBv(String bv) {
        this.bv = bv;
    }

    public langage_while_Vars getLangage_while_vars() {
        return langage_while_vars;
    }

    public void setLangage_while_vars(langage_while_Vars langage_while_vars) {
        this.langage_while_vars = langage_while_vars;
    }
    public langage_while_Input getLangage_while_input() {
        return langage_while_input;
    }

    public void setLangage_while_input(langage_while_Input langage_while_input) {
        this.langage_while_input = langage_while_input;
    }
    public langage_while_Output getLangage_while_output() {
        return langage_while_output;
    }

    public void setLangage_while_output(langage_while_Output langage_while_output) {
        this.langage_while_output = langage_while_output;
    }

}
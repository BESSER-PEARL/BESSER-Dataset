





import java.util.List;
import java.util.ArrayList;

public class whileCpp_ExprSimple  {

    private String nomSymb;
    private String exprHead;
    private String vari;
    private String symb;
    private String nil;
    private String exprTail;



    public whileCpp_ExprSimple(
        String nomSymb,        String exprHead,        String vari,        String symb,        String nil,        String exprTail    ) {
        this.nomSymb = nomSymb;
        this.exprHead = exprHead;
        this.vari = vari;
        this.symb = symb;
        this.nil = nil;
        this.exprTail = exprTail;
    }


    public String getNomsymb() {
        return nomSymb;
    }

    public void setNomsymb(String nomSymb) {
        this.nomSymb = nomSymb;
    }
    public String getExprhead() {
        return exprHead;
    }

    public void setExprhead(String exprHead) {
        this.exprHead = exprHead;
    }
    public String getVari() {
        return vari;
    }

    public void setVari(String vari) {
        this.vari = vari;
    }
    public String getSymb() {
        return symb;
    }

    public void setSymb(String symb) {
        this.symb = symb;
    }
    public String getNil() {
        return nil;
    }

    public void setNil(String nil) {
        this.nil = nil;
    }
    public String getExprtail() {
        return exprTail;
    }

    public void setExprtail(String exprTail) {
        this.exprTail = exprTail;
    }


}
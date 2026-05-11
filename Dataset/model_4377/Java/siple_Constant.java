





import java.util.List;
import java.util.ArrayList;

public class siple_Constant extends Expression {

    private String Lexem;
    private String AsBoolean;
    private String AsInteger;
    private String AsReal;



    public siple_Constant(
        String Lexem,        String AsBoolean,        String AsInteger,        String AsReal    ) {
        super(
        );
        this.Lexem = Lexem;
        this.AsBoolean = AsBoolean;
        this.AsInteger = AsInteger;
        this.AsReal = AsReal;
    }


    public String getLexem() {
        return Lexem;
    }

    public void setLexem(String Lexem) {
        this.Lexem = Lexem;
    }
    public String getAsboolean() {
        return AsBoolean;
    }

    public void setAsboolean(String AsBoolean) {
        this.AsBoolean = AsBoolean;
    }
    public String getAsinteger() {
        return AsInteger;
    }

    public void setAsinteger(String AsInteger) {
        this.AsInteger = AsInteger;
    }
    public String getAsreal() {
        return AsReal;
    }

    public void setAsreal(String AsReal) {
        this.AsReal = AsReal;
    }


}
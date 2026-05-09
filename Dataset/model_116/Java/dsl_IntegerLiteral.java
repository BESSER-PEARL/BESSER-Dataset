





import java.util.List;
import java.util.ArrayList;

public class dsl_IntegerLiteral  {

    private String one;
    private String zero;





    private dsl_SignedIntLiteral dsl_signedintliteral;




    private dsl_UnsignedIntLiteral dsl_unsignedintliteral;




    private dsl_Literal dsl_literal;


    public dsl_IntegerLiteral(
        String one,        String zero    ) {
        this.one = one;
        this.zero = zero;
    }


    public String getOne() {
        return one;
    }

    public void setOne(String one) {
        this.one = one;
    }
    public String getZero() {
        return zero;
    }

    public void setZero(String zero) {
        this.zero = zero;
    }

    public dsl_SignedIntLiteral getDsl_signedintliteral() {
        return dsl_signedintliteral;
    }

    public void setDsl_signedintliteral(dsl_SignedIntLiteral dsl_signedintliteral) {
        this.dsl_signedintliteral = dsl_signedintliteral;
    }
    public dsl_UnsignedIntLiteral getDsl_unsignedintliteral() {
        return dsl_unsignedintliteral;
    }

    public void setDsl_unsignedintliteral(dsl_UnsignedIntLiteral dsl_unsignedintliteral) {
        this.dsl_unsignedintliteral = dsl_unsignedintliteral;
    }
    public dsl_Literal getDsl_literal() {
        return dsl_literal;
    }

    public void setDsl_literal(dsl_Literal dsl_literal) {
        this.dsl_literal = dsl_literal;
    }

}
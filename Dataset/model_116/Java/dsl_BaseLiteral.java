





import java.util.List;
import java.util.ArrayList;

public class dsl_BaseLiteral  {

    private String binDigitsUnderscore;
    private String decDigitsUnderscore;
    private String hexDigitsUnderscore;





    private dsl_SignedIntLiteral dsl_signedintliteral;




    private dsl_UnsignedIntLiteral dsl_unsignedintliteral;


    public dsl_BaseLiteral(
        String binDigitsUnderscore,        String decDigitsUnderscore,        String hexDigitsUnderscore    ) {
        this.binDigitsUnderscore = binDigitsUnderscore;
        this.decDigitsUnderscore = decDigitsUnderscore;
        this.hexDigitsUnderscore = hexDigitsUnderscore;
    }


    public String getBindigitsunderscore() {
        return binDigitsUnderscore;
    }

    public void setBindigitsunderscore(String binDigitsUnderscore) {
        this.binDigitsUnderscore = binDigitsUnderscore;
    }
    public String getDecdigitsunderscore() {
        return decDigitsUnderscore;
    }

    public void setDecdigitsunderscore(String decDigitsUnderscore) {
        this.decDigitsUnderscore = decDigitsUnderscore;
    }
    public String getHexdigitsunderscore() {
        return hexDigitsUnderscore;
    }

    public void setHexdigitsunderscore(String hexDigitsUnderscore) {
        this.hexDigitsUnderscore = hexDigitsUnderscore;
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

}






import java.util.List;
import java.util.ArrayList;

public class delphi_constantDecl extends CSTrace {

    private String port;





    private delphi_constSection delphi_constsection;




    private delphi_constExpr delphi_constexpr;




    private delphi_ident delphi_ident;


    public delphi_constantDecl(
        String port    ) {
        super(
        );
        this.port = port;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }

    public delphi_constSection getDelphi_constsection() {
        return delphi_constsection;
    }

    public void setDelphi_constsection(delphi_constSection delphi_constsection) {
        this.delphi_constsection = delphi_constsection;
    }
    public delphi_constExpr getDelphi_constexpr() {
        return delphi_constexpr;
    }

    public void setDelphi_constexpr(delphi_constExpr delphi_constexpr) {
        this.delphi_constexpr = delphi_constexpr;
    }
    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }

}
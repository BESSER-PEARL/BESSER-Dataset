





import java.util.List;
import java.util.ArrayList;

public class delphi_typeDecl extends CSTrace {

    private String port;





    private delphi_typeSection delphi_typesection;




    private delphi_ident delphi_ident;


    public delphi_typeDecl(
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

    public delphi_typeSection getDelphi_typesection() {
        return delphi_typesection;
    }

    public void setDelphi_typesection(delphi_typeSection delphi_typesection) {
        this.delphi_typesection = delphi_typesection;
    }
    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }

}
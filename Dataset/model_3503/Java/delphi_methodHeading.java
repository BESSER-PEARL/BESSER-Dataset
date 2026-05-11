





import java.util.List;
import java.util.ArrayList;

public class delphi_methodHeading extends CSTrace {






    private delphi_methodList delphi_methodlist;




    private delphi_ident delphi_ident;




    private delphi_formalParameters delphi_formalparameters;


    public delphi_methodHeading(
    ) {
        super(
        );
    }



    public delphi_methodList getDelphi_methodlist() {
        return delphi_methodlist;
    }

    public void setDelphi_methodlist(delphi_methodList delphi_methodlist) {
        this.delphi_methodlist = delphi_methodlist;
    }
    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }
    public delphi_formalParameters getDelphi_formalparameters() {
        return delphi_formalparameters;
    }

    public void setDelphi_formalparameters(delphi_formalParameters delphi_formalparameters) {
        this.delphi_formalparameters = delphi_formalparameters;
    }

}
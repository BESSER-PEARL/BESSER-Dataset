





import java.util.List;
import java.util.ArrayList;

public class delphi_recordFieldConstant extends CSTrace {






    private delphi_ident delphi_ident;




    private delphi_recordConstant delphi_recordconstant;




    private delphi_typedConstant delphi_typedconstant;


    public delphi_recordFieldConstant(
    ) {
        super(
        );
    }



    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }
    public delphi_recordConstant getDelphi_recordconstant() {
        return delphi_recordconstant;
    }

    public void setDelphi_recordconstant(delphi_recordConstant delphi_recordconstant) {
        this.delphi_recordconstant = delphi_recordconstant;
    }
    public delphi_typedConstant getDelphi_typedconstant() {
        return delphi_typedconstant;
    }

    public void setDelphi_typedconstant(delphi_typedConstant delphi_typedconstant) {
        this.delphi_typedconstant = delphi_typedconstant;
    }

}
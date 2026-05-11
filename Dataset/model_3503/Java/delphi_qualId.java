





import java.util.List;
import java.util.ArrayList;

public class delphi_qualId extends CSTrace {






    private delphi_typeId delphi_typeid;




    private delphi_forStmt delphi_forstmt;




    private delphi_ident delphi_ident;


    public delphi_qualId(
    ) {
        super(
        );
    }



    public delphi_typeId getDelphi_typeid() {
        return delphi_typeid;
    }

    public void setDelphi_typeid(delphi_typeId delphi_typeid) {
        this.delphi_typeid = delphi_typeid;
    }
    public delphi_forStmt getDelphi_forstmt() {
        return delphi_forstmt;
    }

    public void setDelphi_forstmt(delphi_forStmt delphi_forstmt) {
        this.delphi_forstmt = delphi_forstmt;
    }
    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }

}
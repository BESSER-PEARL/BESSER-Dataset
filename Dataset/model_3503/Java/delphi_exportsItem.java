





import java.util.List;
import java.util.ArrayList;

public class delphi_exportsItem extends CSTrace {






    private delphi_exportsStmt delphi_exportsstmt;




    private delphi_ident delphi_ident;


    public delphi_exportsItem(
    ) {
        super(
        );
    }



    public delphi_exportsStmt getDelphi_exportsstmt() {
        return delphi_exportsstmt;
    }

    public void setDelphi_exportsstmt(delphi_exportsStmt delphi_exportsstmt) {
        this.delphi_exportsstmt = delphi_exportsstmt;
    }
    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }

}
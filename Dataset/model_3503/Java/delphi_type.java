





import java.util.List;
import java.util.ArrayList;

public class delphi_type extends CSTrace {






    private delphi_functionHeading delphi_functionheading;




    private delphi_identList delphi_identlist;




    private delphi_typeDecl delphi_typedecl;


    public delphi_type(
    ) {
        super(
        );
    }



    public delphi_functionHeading getDelphi_functionheading() {
        return delphi_functionheading;
    }

    public void setDelphi_functionheading(delphi_functionHeading delphi_functionheading) {
        this.delphi_functionheading = delphi_functionheading;
    }
    public delphi_identList getDelphi_identlist() {
        return delphi_identlist;
    }

    public void setDelphi_identlist(delphi_identList delphi_identlist) {
        this.delphi_identlist = delphi_identlist;
    }
    public delphi_typeDecl getDelphi_typedecl() {
        return delphi_typedecl;
    }

    public void setDelphi_typedecl(delphi_typeDecl delphi_typedecl) {
        this.delphi_typedecl = delphi_typedecl;
    }

}
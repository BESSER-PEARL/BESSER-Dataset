





import java.util.List;
import java.util.ArrayList;

public class delphi_variantSection extends CSTrace {






    private delphi_ident delphi_ident;




    private delphi_typeId delphi_typeid;




    private delphi_fieldList delphi_fieldlist;


    public delphi_variantSection(
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
    public delphi_typeId getDelphi_typeid() {
        return delphi_typeid;
    }

    public void setDelphi_typeid(delphi_typeId delphi_typeid) {
        this.delphi_typeid = delphi_typeid;
    }
    public delphi_fieldList getDelphi_fieldlist() {
        return delphi_fieldlist;
    }

    public void setDelphi_fieldlist(delphi_fieldList delphi_fieldlist) {
        this.delphi_fieldlist = delphi_fieldlist;
    }

}
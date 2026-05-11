





import java.util.List;
import java.util.ArrayList;

public class delphi_propertyInterface extends CSTrace {






    private delphi_propertyParameterList delphi_propertyparameterlist;




    private delphi_ident delphi_ident;


    public delphi_propertyInterface(
    ) {
        super(
        );
    }



    public delphi_propertyParameterList getDelphi_propertyparameterlist() {
        return delphi_propertyparameterlist;
    }

    public void setDelphi_propertyparameterlist(delphi_propertyParameterList delphi_propertyparameterlist) {
        this.delphi_propertyparameterlist = delphi_propertyparameterlist;
    }
    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }

}
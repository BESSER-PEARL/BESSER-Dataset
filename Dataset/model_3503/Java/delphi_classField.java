





import java.util.List;
import java.util.ArrayList;

public class delphi_classField extends CSTrace {

    private String visibility;





    private delphi_classFieldList delphi_classfieldlist;




    private delphi_objFieldList delphi_objfieldlist;


    public delphi_classField(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public delphi_classFieldList getDelphi_classfieldlist() {
        return delphi_classfieldlist;
    }

    public void setDelphi_classfieldlist(delphi_classFieldList delphi_classfieldlist) {
        this.delphi_classfieldlist = delphi_classfieldlist;
    }
    public delphi_objFieldList getDelphi_objfieldlist() {
        return delphi_objfieldlist;
    }

    public void setDelphi_objfieldlist(delphi_objFieldList delphi_objfieldlist) {
        this.delphi_objfieldlist = delphi_objfieldlist;
    }

}
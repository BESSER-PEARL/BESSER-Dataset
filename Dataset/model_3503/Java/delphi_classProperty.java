





import java.util.List;
import java.util.ArrayList;

public class delphi_classProperty extends CSTrace {

    private String visibility;





    private delphi_classPropertyList delphi_classpropertylist;


    public delphi_classProperty(
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

    public delphi_classPropertyList getDelphi_classpropertylist() {
        return delphi_classpropertylist;
    }

    public void setDelphi_classpropertylist(delphi_classPropertyList delphi_classpropertylist) {
        this.delphi_classpropertylist = delphi_classpropertylist;
    }

}
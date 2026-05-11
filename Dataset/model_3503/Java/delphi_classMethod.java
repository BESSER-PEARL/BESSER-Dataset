





import java.util.List;
import java.util.ArrayList;

public class delphi_classMethod extends CSTrace {

    private String visibility;





    private delphi_classMethodList delphi_classmethodlist;




    private delphi_methodList delphi_methodlist;


    public delphi_classMethod(
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

    public delphi_classMethodList getDelphi_classmethodlist() {
        return delphi_classmethodlist;
    }

    public void setDelphi_classmethodlist(delphi_classMethodList delphi_classmethodlist) {
        this.delphi_classmethodlist = delphi_classmethodlist;
    }
    public delphi_methodList getDelphi_methodlist() {
        return delphi_methodlist;
    }

    public void setDelphi_methodlist(delphi_methodList delphi_methodlist) {
        this.delphi_methodlist = delphi_methodlist;
    }

}
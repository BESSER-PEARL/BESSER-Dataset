





import java.util.List;
import java.util.ArrayList;

public class scxml_Donedata  {






    private scxml_FinalState scxml_finalstate;




    private List<scxml_Param> scxml_params;


    public scxml_Donedata(
    ) {
        this.scxml_params = new ArrayList<>();
    }

    public scxml_Donedata(
        ArrayList<scxml_Param> scxml_params    ) {
        this.scxml_params = scxml_params;
    }


    public scxml_FinalState getScxml_finalstate() {
        return scxml_finalstate;
    }

    public void setScxml_finalstate(scxml_FinalState scxml_finalstate) {
        this.scxml_finalstate = scxml_finalstate;
    }
    public List<scxml_Param> getScxml_params() {
        return scxml_params;
    }

    public void addScxml_param(Scxml_param scxml_param) {
        this.scxml_params.add(scxml_param);
    }

}
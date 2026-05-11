





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractMTypeContainer  {






    private jsm_AbstractMDeclaredType jsm_abstractmdeclaredtype;




    private List<jsm_AbstractMDeclaredType> jsm_abstractmdeclaredtypes;


    public jsm_AbstractMTypeContainer(
    ) {
        this.jsm_abstractmdeclaredtypes = new ArrayList<>();
    }

    public jsm_AbstractMTypeContainer(
        ArrayList<jsm_AbstractMDeclaredType> jsm_abstractmdeclaredtypes    ) {
        this.jsm_abstractmdeclaredtypes = jsm_abstractmdeclaredtypes;
    }


    public jsm_AbstractMDeclaredType getJsm_abstractmdeclaredtype() {
        return jsm_abstractmdeclaredtype;
    }

    public void setJsm_abstractmdeclaredtype(jsm_AbstractMDeclaredType jsm_abstractmdeclaredtype) {
        this.jsm_abstractmdeclaredtype = jsm_abstractmdeclaredtype;
    }
    public List<jsm_AbstractMDeclaredType> getJsm_abstractmdeclaredtypes() {
        return jsm_abstractmdeclaredtypes;
    }

    public void addJsm_abstractmdeclaredtype(Jsm_abstractmdeclaredtype jsm_abstractmdeclaredtype) {
        this.jsm_abstractmdeclaredtypes.add(jsm_abstractmdeclaredtype);
    }

}
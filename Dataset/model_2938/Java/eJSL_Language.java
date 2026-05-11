





import java.util.List;
import java.util.ArrayList;

public class eJSL_Language  {

    private boolean sys;
    private String name;





    private eJSL_Extension ejsl_extension;




    private List<eJSL_KeyValuePair> ejsl_keyvaluepairs;


    public eJSL_Language(
        boolean sys,        String name    ) {
        this.sys = sys;
        this.name = name;
        this.ejsl_keyvaluepairs = new ArrayList<>();
    }

    public eJSL_Language(
        boolean sys,        String name        ArrayList<eJSL_KeyValuePair> ejsl_keyvaluepairs    ) {
        this.sys = sys;
        this.name = name;
        this.ejsl_keyvaluepairs = ejsl_keyvaluepairs;
    }

    public boolean getSys() {
        return sys;
    }

    public void setSys(boolean sys) {
        this.sys = sys;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_Extension getEjsl_extension() {
        return ejsl_extension;
    }

    public void setEjsl_extension(eJSL_Extension ejsl_extension) {
        this.ejsl_extension = ejsl_extension;
    }
    public List<eJSL_KeyValuePair> getEjsl_keyvaluepairs() {
        return ejsl_keyvaluepairs;
    }

    public void addEjsl_keyvaluepair(Ejsl_keyvaluepair ejsl_keyvaluepair) {
        this.ejsl_keyvaluepairs.add(ejsl_keyvaluepair);
    }

}
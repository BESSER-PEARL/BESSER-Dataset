





import java.util.List;
import java.util.ArrayList;

public class urml_Operation  {

    private String name;
    private boolean isBool;
    private boolean isInt;
    private boolean isVoid;





    private urml_Capsule urml_capsule;




    private List<urml_LocalVar> urml_localvars;


    public urml_Operation(
        String name,        boolean isBool,        boolean isInt,        boolean isVoid    ) {
        this.name = name;
        this.isBool = isBool;
        this.isInt = isInt;
        this.isVoid = isVoid;
        this.urml_localvars = new ArrayList<>();
    }

    public urml_Operation(
        String name,        boolean isBool,        boolean isInt,        boolean isVoid        ArrayList<urml_LocalVar> urml_localvars    ) {
        this.name = name;
        this.isBool = isBool;
        this.isInt = isInt;
        this.isVoid = isVoid;
        this.urml_localvars = urml_localvars;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsbool() {
        return isBool;
    }

    public void setIsbool(boolean isBool) {
        this.isBool = isBool;
    }
    public boolean getIsint() {
        return isInt;
    }

    public void setIsint(boolean isInt) {
        this.isInt = isInt;
    }
    public boolean getIsvoid() {
        return isVoid;
    }

    public void setIsvoid(boolean isVoid) {
        this.isVoid = isVoid;
    }

    public urml_Capsule getUrml_capsule() {
        return urml_capsule;
    }

    public void setUrml_capsule(urml_Capsule urml_capsule) {
        this.urml_capsule = urml_capsule;
    }
    public List<urml_LocalVar> getUrml_localvars() {
        return urml_localvars;
    }

    public void addUrml_localvar(Urml_localvar urml_localvar) {
        this.urml_localvars.add(urml_localvar);
    }

}
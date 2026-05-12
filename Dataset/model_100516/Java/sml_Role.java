





import java.util.List;
import java.util.ArrayList;

public class sml_Role  {

    private boolean static;
    private String name;





    private sml_Collaboration sml_collaboration;




    private sml_SmlEClass sml_smleclass;


    public sml_Role(
        boolean static,        String name    ) {
        this.static = static;
        this.name = name;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_Collaboration getSml_collaboration() {
        return sml_collaboration;
    }

    public void setSml_collaboration(sml_Collaboration sml_collaboration) {
        this.sml_collaboration = sml_collaboration;
    }
    public sml_SmlEClass getSml_smleclass() {
        return sml_smleclass;
    }

    public void setSml_smleclass(sml_SmlEClass sml_smleclass) {
        this.sml_smleclass = sml_smleclass;
    }

}
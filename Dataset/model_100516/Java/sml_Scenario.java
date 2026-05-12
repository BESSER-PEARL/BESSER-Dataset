





import java.util.List;
import java.util.ArrayList;

public class sml_Scenario  {

    private String kind;
    private boolean singular;
    private String name;





    private sml_Collaboration sml_collaboration;


    public sml_Scenario(
        String kind,        boolean singular,        String name    ) {
        this.kind = kind;
        this.singular = singular;
        this.name = name;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public boolean getSingular() {
        return singular;
    }

    public void setSingular(boolean singular) {
        this.singular = singular;
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

}
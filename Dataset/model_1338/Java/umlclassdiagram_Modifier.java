





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Modifier extends NamedElement {

    private String visibility;
    private String scope;



    public umlclassdiagram_Modifier(
        String visibility,        String scope    ) {
        super(
        );
        this.visibility = visibility;
        this.scope = scope;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}
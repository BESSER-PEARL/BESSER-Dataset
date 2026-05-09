





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Feature  {

    private String scope;
    private String visibility;
    private String name;





    private umlclassdiagram_PathElementCS umlclassdiagram_pathelementcs;


    public umlclassdiagram_Feature(
        String scope,        String visibility,        String name    ) {
        this.scope = scope;
        this.visibility = visibility;
        this.name = name;
    }


    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umlclassdiagram_PathElementCS getUmlclassdiagram_pathelementcs() {
        return umlclassdiagram_pathelementcs;
    }

    public void setUmlclassdiagram_pathelementcs(umlclassdiagram_PathElementCS umlclassdiagram_pathelementcs) {
        this.umlclassdiagram_pathelementcs = umlclassdiagram_pathelementcs;
    }

}
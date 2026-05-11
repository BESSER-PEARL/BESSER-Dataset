





import java.util.List;
import java.util.ArrayList;

public class oogen_OOMember extends OOVariable {

    private String visibility;
    private boolean static;
    private String languages;





    private oogen_OOClass oogen_ooclass;


    public oogen_OOMember(
        String visibility,        boolean static,        String languages    ) {
        super(
        );
        this.visibility = visibility;
        this.static = static;
        this.languages = languages;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getLanguages() {
        return languages;
    }

    public void setLanguages(String languages) {
        this.languages = languages;
    }

    public oogen_OOClass getOogen_ooclass() {
        return oogen_ooclass;
    }

    public void setOogen_ooclass(oogen_OOClass oogen_ooclass) {
        this.oogen_ooclass = oogen_ooclass;
    }

}
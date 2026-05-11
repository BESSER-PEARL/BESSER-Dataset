





import java.util.List;
import java.util.ArrayList;

public class oogen_OOMethod extends OOCommentOwner {

    private String name;
    private String visibility;
    private String languages;
    private boolean static;





    private oogen_OOClass oogen_ooclass;




    private List<oogen_OOStatement> oogen_oostatements;


    public oogen_OOMethod(
        String name,        String visibility,        String languages,        boolean static    ) {
        super(
        );
        this.name = name;
        this.visibility = visibility;
        this.languages = languages;
        this.static = static;
        this.oogen_oostatements = new ArrayList<>();
    }

    public oogen_OOMethod(
        String name,        String visibility,        String languages,        boolean static        ArrayList<oogen_OOStatement> oogen_oostatements    ) {
        this.name = name;
        this.visibility = visibility;
        this.languages = languages;
        this.static = static;
        this.oogen_oostatements = oogen_oostatements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getLanguages() {
        return languages;
    }

    public void setLanguages(String languages) {
        this.languages = languages;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public oogen_OOClass getOogen_ooclass() {
        return oogen_ooclass;
    }

    public void setOogen_ooclass(oogen_OOClass oogen_ooclass) {
        this.oogen_ooclass = oogen_ooclass;
    }
    public List<oogen_OOStatement> getOogen_oostatements() {
        return oogen_oostatements;
    }

    public void addOogen_oostatement(Oogen_oostatement oogen_oostatement) {
        this.oogen_oostatements.add(oogen_oostatement);
    }

}
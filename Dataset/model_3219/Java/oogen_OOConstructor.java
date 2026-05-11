





import java.util.List;
import java.util.ArrayList;

public class oogen_OOConstructor  {

    private String visibility;
    private String className;





    private oogen_OOClass oogen_ooclass;




    private List<oogen_OOStatement> oogen_oostatements;


    public oogen_OOConstructor(
        String visibility,        String className    ) {
        this.visibility = visibility;
        this.className = className;
        this.oogen_oostatements = new ArrayList<>();
    }

    public oogen_OOConstructor(
        String visibility,        String className        ArrayList<oogen_OOStatement> oogen_oostatements    ) {
        this.visibility = visibility;
        this.className = className;
        this.oogen_oostatements = oogen_oostatements;
    }

    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
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
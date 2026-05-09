





import java.util.List;
import java.util.ArrayList;

public class UMLModel_CollaborationUse extends NamedElement {

    private String type;





    private List<UMLModel_Dependency> umlmodel_dependencys;


    public UMLModel_CollaborationUse(
        String type    ) {
        super(
        );
        this.type = type;
        this.umlmodel_dependencys = new ArrayList<>();
    }

    public UMLModel_CollaborationUse(
        String type        ArrayList<UMLModel_Dependency> umlmodel_dependencys    ) {
        this.type = type;
        this.umlmodel_dependencys = umlmodel_dependencys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<UMLModel_Dependency> getUmlmodel_dependencys() {
        return umlmodel_dependencys;
    }

    public void addUmlmodel_dependency(Umlmodel_dependency umlmodel_dependency) {
        this.umlmodel_dependencys.add(umlmodel_dependency);
    }

}






import java.util.List;
import java.util.ArrayList;

public class UMLModel_Namespace extends NamedElement {

    private String ownedMember;
    private String member;
    private String importedMember;





    private List<UMLModel_ElementImport> umlmodel_elementimports;




    private List<UMLModel_PackageImport> umlmodel_packageimports;




    private List<UMLModel_Constraint> umlmodel_constraints;


    public UMLModel_Namespace(
        String ownedMember,        String member,        String importedMember    ) {
        super(
        );
        this.ownedMember = ownedMember;
        this.member = member;
        this.importedMember = importedMember;
        this.umlmodel_elementimports = new ArrayList<>();
        this.umlmodel_packageimports = new ArrayList<>();
        this.umlmodel_constraints = new ArrayList<>();
    }

    public UMLModel_Namespace(
        String ownedMember,        String member,        String importedMember        ArrayList<UMLModel_ElementImport> umlmodel_elementimports,        ArrayList<UMLModel_PackageImport> umlmodel_packageimports,        ArrayList<UMLModel_Constraint> umlmodel_constraints    ) {
        this.ownedMember = ownedMember;
        this.member = member;
        this.importedMember = importedMember;
        this.umlmodel_elementimports = umlmodel_elementimports;
        this.umlmodel_packageimports = umlmodel_packageimports;
        this.umlmodel_constraints = umlmodel_constraints;
    }

    public String getOwnedmember() {
        return ownedMember;
    }

    public void setOwnedmember(String ownedMember) {
        this.ownedMember = ownedMember;
    }
    public String getMember() {
        return member;
    }

    public void setMember(String member) {
        this.member = member;
    }
    public String getImportedmember() {
        return importedMember;
    }

    public void setImportedmember(String importedMember) {
        this.importedMember = importedMember;
    }

    public List<UMLModel_ElementImport> getUmlmodel_elementimports() {
        return umlmodel_elementimports;
    }

    public void addUmlmodel_elementimport(Umlmodel_elementimport umlmodel_elementimport) {
        this.umlmodel_elementimports.add(umlmodel_elementimport);
    }
    public List<UMLModel_PackageImport> getUmlmodel_packageimports() {
        return umlmodel_packageimports;
    }

    public void addUmlmodel_packageimport(Umlmodel_packageimport umlmodel_packageimport) {
        this.umlmodel_packageimports.add(umlmodel_packageimport);
    }
    public List<UMLModel_Constraint> getUmlmodel_constraints() {
        return umlmodel_constraints;
    }

    public void addUmlmodel_constraint(Umlmodel_constraint umlmodel_constraint) {
        this.umlmodel_constraints.add(umlmodel_constraint);
    }

}






import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_PackageToSchema extends UmlToRdbmsModelElement {






    private uml2rdbms_ClassToTable uml2rdbms_classtotable;




    private List<uml2rdbms_ClassToTable> uml2rdbms_classtotables;


    public uml2rdbms_PackageToSchema(
    ) {
        super(
        );
        this.uml2rdbms_classtotables = new ArrayList<>();
    }

    public uml2rdbms_PackageToSchema(
        ArrayList<uml2rdbms_ClassToTable> uml2rdbms_classtotables    ) {
        this.uml2rdbms_classtotables = uml2rdbms_classtotables;
    }


    public uml2rdbms_ClassToTable getUml2rdbms_classtotable() {
        return uml2rdbms_classtotable;
    }

    public void setUml2rdbms_classtotable(uml2rdbms_ClassToTable uml2rdbms_classtotable) {
        this.uml2rdbms_classtotable = uml2rdbms_classtotable;
    }
    public List<uml2rdbms_ClassToTable> getUml2rdbms_classtotables() {
        return uml2rdbms_classtotables;
    }

    public void addUml2rdbms_classtotable(Uml2rdbms_classtotable uml2rdbms_classtotable) {
        this.uml2rdbms_classtotables.add(uml2rdbms_classtotable);
    }

}
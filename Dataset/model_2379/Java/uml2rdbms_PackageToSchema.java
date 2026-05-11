





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_PackageToSchema  {

    private String name;





    private List<uml2rdbms_ClassToTable> uml2rdbms_classtotables;




    private uml2rdbms_ClassToTable uml2rdbms_classtotable;




    private List<uml2rdbms_PrimitiveToName> uml2rdbms_primitivetonames;




    private uml2rdbms_PrimitiveToName uml2rdbms_primitivetoname;


    public uml2rdbms_PackageToSchema(
        String name    ) {
        this.name = name;
        this.uml2rdbms_classtotables = new ArrayList<>();
        this.uml2rdbms_primitivetonames = new ArrayList<>();
    }

    public uml2rdbms_PackageToSchema(
        String name        ArrayList<uml2rdbms_ClassToTable> uml2rdbms_classtotables,        ArrayList<uml2rdbms_PrimitiveToName> uml2rdbms_primitivetonames    ) {
        this.name = name;
        this.uml2rdbms_classtotables = uml2rdbms_classtotables;
        this.uml2rdbms_primitivetonames = uml2rdbms_primitivetonames;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<uml2rdbms_ClassToTable> getUml2rdbms_classtotables() {
        return uml2rdbms_classtotables;
    }

    public void addUml2rdbms_classtotable(Uml2rdbms_classtotable uml2rdbms_classtotable) {
        this.uml2rdbms_classtotables.add(uml2rdbms_classtotable);
    }
    public uml2rdbms_ClassToTable getUml2rdbms_classtotable() {
        return uml2rdbms_classtotable;
    }

    public void setUml2rdbms_classtotable(uml2rdbms_ClassToTable uml2rdbms_classtotable) {
        this.uml2rdbms_classtotable = uml2rdbms_classtotable;
    }
    public List<uml2rdbms_PrimitiveToName> getUml2rdbms_primitivetonames() {
        return uml2rdbms_primitivetonames;
    }

    public void addUml2rdbms_primitivetoname(Uml2rdbms_primitivetoname uml2rdbms_primitivetoname) {
        this.uml2rdbms_primitivetonames.add(uml2rdbms_primitivetoname);
    }
    public uml2rdbms_PrimitiveToName getUml2rdbms_primitivetoname() {
        return uml2rdbms_primitivetoname;
    }

    public void setUml2rdbms_primitivetoname(uml2rdbms_PrimitiveToName uml2rdbms_primitivetoname) {
        this.uml2rdbms_primitivetoname = uml2rdbms_primitivetoname;
    }

}
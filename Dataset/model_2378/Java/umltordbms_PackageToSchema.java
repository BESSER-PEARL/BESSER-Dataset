





import java.util.List;
import java.util.ArrayList;

public class umltordbms_PackageToSchema  {

    private String name;





    private umltordbms_PrimitiveToName umltordbms_primitivetoname;




    private List<umltordbms_PrimitiveToName> umltordbms_primitivetonames;




    private List<umltordbms_ClassToTable> umltordbms_classtotables;




    private umltordbms_ClassToTable umltordbms_classtotable;


    public umltordbms_PackageToSchema(
        String name    ) {
        this.name = name;
        this.umltordbms_primitivetonames = new ArrayList<>();
        this.umltordbms_classtotables = new ArrayList<>();
    }

    public umltordbms_PackageToSchema(
        String name        ArrayList<umltordbms_PrimitiveToName> umltordbms_primitivetonames,        ArrayList<umltordbms_ClassToTable> umltordbms_classtotables    ) {
        this.name = name;
        this.umltordbms_primitivetonames = umltordbms_primitivetonames;
        this.umltordbms_classtotables = umltordbms_classtotables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umltordbms_PrimitiveToName getUmltordbms_primitivetoname() {
        return umltordbms_primitivetoname;
    }

    public void setUmltordbms_primitivetoname(umltordbms_PrimitiveToName umltordbms_primitivetoname) {
        this.umltordbms_primitivetoname = umltordbms_primitivetoname;
    }
    public List<umltordbms_PrimitiveToName> getUmltordbms_primitivetonames() {
        return umltordbms_primitivetonames;
    }

    public void addUmltordbms_primitivetoname(Umltordbms_primitivetoname umltordbms_primitivetoname) {
        this.umltordbms_primitivetonames.add(umltordbms_primitivetoname);
    }
    public List<umltordbms_ClassToTable> getUmltordbms_classtotables() {
        return umltordbms_classtotables;
    }

    public void addUmltordbms_classtotable(Umltordbms_classtotable umltordbms_classtotable) {
        this.umltordbms_classtotables.add(umltordbms_classtotable);
    }
    public umltordbms_ClassToTable getUmltordbms_classtotable() {
        return umltordbms_classtotable;
    }

    public void setUmltordbms_classtotable(umltordbms_ClassToTable umltordbms_classtotable) {
        this.umltordbms_classtotable = umltordbms_classtotable;
    }

}
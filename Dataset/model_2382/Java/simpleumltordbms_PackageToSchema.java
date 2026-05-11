





import java.util.List;
import java.util.ArrayList;

public class simpleumltordbms_PackageToSchema extends UmlToRdbmsModelElement {






    private simpleumltordbms_ClassToTable simpleumltordbms_classtotable;




    private simpleumltordbms_PrimitiveToName simpleumltordbms_primitivetoname;




    private List<simpleumltordbms_ClassToTable> simpleumltordbms_classtotables;




    private List<simpleumltordbms_PrimitiveToName> simpleumltordbms_primitivetonames;


    public simpleumltordbms_PackageToSchema(
    ) {
        super(
        );
        this.simpleumltordbms_classtotables = new ArrayList<>();
        this.simpleumltordbms_primitivetonames = new ArrayList<>();
    }

    public simpleumltordbms_PackageToSchema(
        ArrayList<simpleumltordbms_ClassToTable> simpleumltordbms_classtotables,        ArrayList<simpleumltordbms_PrimitiveToName> simpleumltordbms_primitivetonames    ) {
        this.simpleumltordbms_classtotables = simpleumltordbms_classtotables;
        this.simpleumltordbms_primitivetonames = simpleumltordbms_primitivetonames;
    }


    public simpleumltordbms_ClassToTable getSimpleumltordbms_classtotable() {
        return simpleumltordbms_classtotable;
    }

    public void setSimpleumltordbms_classtotable(simpleumltordbms_ClassToTable simpleumltordbms_classtotable) {
        this.simpleumltordbms_classtotable = simpleumltordbms_classtotable;
    }
    public simpleumltordbms_PrimitiveToName getSimpleumltordbms_primitivetoname() {
        return simpleumltordbms_primitivetoname;
    }

    public void setSimpleumltordbms_primitivetoname(simpleumltordbms_PrimitiveToName simpleumltordbms_primitivetoname) {
        this.simpleumltordbms_primitivetoname = simpleumltordbms_primitivetoname;
    }
    public List<simpleumltordbms_ClassToTable> getSimpleumltordbms_classtotables() {
        return simpleumltordbms_classtotables;
    }

    public void addSimpleumltordbms_classtotable(Simpleumltordbms_classtotable simpleumltordbms_classtotable) {
        this.simpleumltordbms_classtotables.add(simpleumltordbms_classtotable);
    }
    public List<simpleumltordbms_PrimitiveToName> getSimpleumltordbms_primitivetonames() {
        return simpleumltordbms_primitivetonames;
    }

    public void addSimpleumltordbms_primitivetoname(Simpleumltordbms_primitivetoname simpleumltordbms_primitivetoname) {
        this.simpleumltordbms_primitivetonames.add(simpleumltordbms_primitivetoname);
    }

}
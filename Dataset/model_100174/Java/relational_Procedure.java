





import java.util.List;
import java.util.ArrayList;

public class relational_Procedure extends RelationalEntity {

    private boolean function;
    private String updateCount;





    private List<relational_ProcedureParameter> relational_procedureparameters;




    private relational_Catalog relational_catalog;




    private relational_ProcedureResult relational_procedureresult;




    private relational_Schema relational_schema;




    private relational_Schema relational_schema;




    private relational_ProcedureResult relational_procedureresult;




    private relational_Catalog relational_catalog;




    private relational_ProcedureParameter relational_procedureparameter;


    public relational_Procedure(
        boolean function,        String updateCount    ) {
        super(
        );
        this.function = function;
        this.updateCount = updateCount;
        this.relational_procedureparameters = new ArrayList<>();
    }

    public relational_Procedure(
        boolean function,        String updateCount        ArrayList<relational_ProcedureParameter> relational_procedureparameters    ) {
        this.function = function;
        this.updateCount = updateCount;
        this.relational_procedureparameters = relational_procedureparameters;
    }

    public boolean getFunction() {
        return function;
    }

    public void setFunction(boolean function) {
        this.function = function;
    }
    public String getUpdatecount() {
        return updateCount;
    }

    public void setUpdatecount(String updateCount) {
        this.updateCount = updateCount;
    }

    public List<relational_ProcedureParameter> getRelational_procedureparameters() {
        return relational_procedureparameters;
    }

    public void addRelational_procedureparameter(Relational_procedureparameter relational_procedureparameter) {
        this.relational_procedureparameters.add(relational_procedureparameter);
    }
    public relational_Catalog getRelational_catalog() {
        return relational_catalog;
    }

    public void setRelational_catalog(relational_Catalog relational_catalog) {
        this.relational_catalog = relational_catalog;
    }
    public relational_ProcedureResult getRelational_procedureresult() {
        return relational_procedureresult;
    }

    public void setRelational_procedureresult(relational_ProcedureResult relational_procedureresult) {
        this.relational_procedureresult = relational_procedureresult;
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public relational_ProcedureResult getRelational_procedureresult() {
        return relational_procedureresult;
    }

    public void setRelational_procedureresult(relational_ProcedureResult relational_procedureresult) {
        this.relational_procedureresult = relational_procedureresult;
    }
    public relational_Catalog getRelational_catalog() {
        return relational_catalog;
    }

    public void setRelational_catalog(relational_Catalog relational_catalog) {
        this.relational_catalog = relational_catalog;
    }
    public relational_ProcedureParameter getRelational_procedureparameter() {
        return relational_procedureparameter;
    }

    public void setRelational_procedureparameter(relational_ProcedureParameter relational_procedureparameter) {
        this.relational_procedureparameter = relational_procedureparameter;
    }

}
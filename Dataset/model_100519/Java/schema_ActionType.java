





import java.util.List;
import java.util.ArrayList;

public class schema_ActionType  {

    private String status;





    private List<schema_TargetTypeRef> schema_targettyperefs;




    private schema_StorySchemaCatalog schema_storyschemacatalog;


    public schema_ActionType(
        String status    ) {
        this.status = status;
        this.schema_targettyperefs = new ArrayList<>();
    }

    public schema_ActionType(
        String status        ArrayList<schema_TargetTypeRef> schema_targettyperefs    ) {
        this.status = status;
        this.schema_targettyperefs = schema_targettyperefs;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<schema_TargetTypeRef> getSchema_targettyperefs() {
        return schema_targettyperefs;
    }

    public void addSchema_targettyperef(Schema_targettyperef schema_targettyperef) {
        this.schema_targettyperefs.add(schema_targettyperef);
    }
    public schema_StorySchemaCatalog getSchema_storyschemacatalog() {
        return schema_storyschemacatalog;
    }

    public void setSchema_storyschemacatalog(schema_StorySchemaCatalog schema_storyschemacatalog) {
        this.schema_storyschemacatalog = schema_storyschemacatalog;
    }

}






import java.util.List;
import java.util.ArrayList;

public class relationalMetaModel_RelationalSchema  {

    private String Name;





    private List<relationalMetaModel_RelationalTable> relationalmetamodel_relationaltables;




    private relationalMetaModel_RelationalTable relationalmetamodel_relationaltable;


    public relationalMetaModel_RelationalSchema(
        String Name    ) {
        this.Name = Name;
        this.relationalmetamodel_relationaltables = new ArrayList<>();
    }

    public relationalMetaModel_RelationalSchema(
        String Name        ArrayList<relationalMetaModel_RelationalTable> relationalmetamodel_relationaltables    ) {
        this.Name = Name;
        this.relationalmetamodel_relationaltables = relationalmetamodel_relationaltables;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<relationalMetaModel_RelationalTable> getRelationalmetamodel_relationaltables() {
        return relationalmetamodel_relationaltables;
    }

    public void addRelationalmetamodel_relationaltable(Relationalmetamodel_relationaltable relationalmetamodel_relationaltable) {
        this.relationalmetamodel_relationaltables.add(relationalmetamodel_relationaltable);
    }
    public relationalMetaModel_RelationalTable getRelationalmetamodel_relationaltable() {
        return relationalmetamodel_relationaltable;
    }

    public void setRelationalmetamodel_relationaltable(relationalMetaModel_RelationalTable relationalmetamodel_relationaltable) {
        this.relationalmetamodel_relationaltable = relationalmetamodel_relationaltable;
    }

}
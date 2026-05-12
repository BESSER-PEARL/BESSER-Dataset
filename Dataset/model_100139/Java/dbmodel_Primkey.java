





import java.util.List;
import java.util.ArrayList;

public class dbmodel_Primkey  {






    private dbmodel_Class dbmodel_class;




    private List<dbmodel_Attribute> dbmodel_attributes;


    public dbmodel_Primkey(
    ) {
        this.dbmodel_attributes = new ArrayList<>();
    }

    public dbmodel_Primkey(
        ArrayList<dbmodel_Attribute> dbmodel_attributes    ) {
        this.dbmodel_attributes = dbmodel_attributes;
    }


    public dbmodel_Class getDbmodel_class() {
        return dbmodel_class;
    }

    public void setDbmodel_class(dbmodel_Class dbmodel_class) {
        this.dbmodel_class = dbmodel_class;
    }
    public List<dbmodel_Attribute> getDbmodel_attributes() {
        return dbmodel_attributes;
    }

    public void addDbmodel_attribute(Dbmodel_attribute dbmodel_attribute) {
        this.dbmodel_attributes.add(dbmodel_attribute);
    }

}
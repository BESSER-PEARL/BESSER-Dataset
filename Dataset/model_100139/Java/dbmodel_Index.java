





import java.util.List;
import java.util.ArrayList;

public class dbmodel_Index  {

    private boolean kuko;
    private boolean unique;
    private String name;





    private dbmodel_Class dbmodel_class;


    public dbmodel_Index(
        boolean kuko,        boolean unique,        String name    ) {
        this.kuko = kuko;
        this.unique = unique;
        this.name = name;
    }


    public boolean getKuko() {
        return kuko;
    }

    public void setKuko(boolean kuko) {
        this.kuko = kuko;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbmodel_Class getDbmodel_class() {
        return dbmodel_class;
    }

    public void setDbmodel_class(dbmodel_Class dbmodel_class) {
        this.dbmodel_class = dbmodel_class;
    }

}
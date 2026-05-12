





import java.util.List;
import java.util.ArrayList;

public class dbmodel_IndexRef  {

    private boolean clustered;
    private boolean isPrimkey;





    private dbmodel_Pdb dbmodel_pdb;




    private dbmodel_Index dbmodel_index;




    private dbmodel_Attribute dbmodel_attribute;


    public dbmodel_IndexRef(
        boolean clustered,        boolean isPrimkey    ) {
        this.clustered = clustered;
        this.isPrimkey = isPrimkey;
    }


    public boolean getClustered() {
        return clustered;
    }

    public void setClustered(boolean clustered) {
        this.clustered = clustered;
    }
    public boolean getIsprimkey() {
        return isPrimkey;
    }

    public void setIsprimkey(boolean isPrimkey) {
        this.isPrimkey = isPrimkey;
    }

    public dbmodel_Pdb getDbmodel_pdb() {
        return dbmodel_pdb;
    }

    public void setDbmodel_pdb(dbmodel_Pdb dbmodel_pdb) {
        this.dbmodel_pdb = dbmodel_pdb;
    }
    public dbmodel_Index getDbmodel_index() {
        return dbmodel_index;
    }

    public void setDbmodel_index(dbmodel_Index dbmodel_index) {
        this.dbmodel_index = dbmodel_index;
    }
    public dbmodel_Attribute getDbmodel_attribute() {
        return dbmodel_attribute;
    }

    public void setDbmodel_attribute(dbmodel_Attribute dbmodel_attribute) {
        this.dbmodel_attribute = dbmodel_attribute;
    }

}
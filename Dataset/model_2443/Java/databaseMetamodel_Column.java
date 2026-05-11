





import java.util.List;
import java.util.ArrayList;

public class databaseMetamodel_Column  {

    private int hasPKOrder;
    private String type;
    private int hasFKOrder;
    private String name;





    private databaseMetamodel_Column databasemetamodel_column;


    public databaseMetamodel_Column(
        int hasPKOrder,        String type,        int hasFKOrder,        String name    ) {
        this.hasPKOrder = hasPKOrder;
        this.type = type;
        this.hasFKOrder = hasFKOrder;
        this.name = name;
    }


    public int getHaspkorder() {
        return hasPKOrder;
    }

    public void setHaspkorder(int hasPKOrder) {
        this.hasPKOrder = hasPKOrder;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getHasfkorder() {
        return hasFKOrder;
    }

    public void setHasfkorder(int hasFKOrder) {
        this.hasFKOrder = hasFKOrder;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public databaseMetamodel_Column getDatabasemetamodel_column() {
        return databasemetamodel_column;
    }

    public void setDatabasemetamodel_column(databaseMetamodel_Column databasemetamodel_column) {
        this.databasemetamodel_column = databasemetamodel_column;
    }

}
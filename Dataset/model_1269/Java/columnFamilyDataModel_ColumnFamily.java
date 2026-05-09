





import java.util.List;
import java.util.ArrayList;

public class columnFamilyDataModel_ColumnFamily  {

    private String name;





    private columnFamilyDataModel_Column columnfamilydatamodel_column;




    private columnFamilyDataModel_Table columnfamilydatamodel_table;


    public columnFamilyDataModel_ColumnFamily(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public columnFamilyDataModel_Column getColumnfamilydatamodel_column() {
        return columnfamilydatamodel_column;
    }

    public void setColumnfamilydatamodel_column(columnFamilyDataModel_Column columnfamilydatamodel_column) {
        this.columnfamilydatamodel_column = columnfamilydatamodel_column;
    }
    public columnFamilyDataModel_Table getColumnfamilydatamodel_table() {
        return columnfamilydatamodel_table;
    }

    public void setColumnfamilydatamodel_table(columnFamilyDataModel_Table columnfamilydatamodel_table) {
        this.columnfamilydatamodel_table = columnfamilydatamodel_table;
    }

}
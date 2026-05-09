





import java.util.List;
import java.util.ArrayList;

public class columnFamilyDataModel_Table  {

    private String name;





    private List<columnFamilyDataModel_PartitionKey> columnfamilydatamodel_partitionkeys;




    private List<columnFamilyDataModel_ClusteringKey> columnfamilydatamodel_clusteringkeys;




    private List<columnFamilyDataModel_Column> columnfamilydatamodel_columns;




    private columnFamilyDataModel_ColumnFamilyDataModel columnfamilydatamodel_columnfamilydatamodel;


    public columnFamilyDataModel_Table(
        String name    ) {
        this.name = name;
        this.columnfamilydatamodel_partitionkeys = new ArrayList<>();
        this.columnfamilydatamodel_clusteringkeys = new ArrayList<>();
        this.columnfamilydatamodel_columns = new ArrayList<>();
    }

    public columnFamilyDataModel_Table(
        String name        ArrayList<columnFamilyDataModel_PartitionKey> columnfamilydatamodel_partitionkeys,        ArrayList<columnFamilyDataModel_ClusteringKey> columnfamilydatamodel_clusteringkeys,        ArrayList<columnFamilyDataModel_Column> columnfamilydatamodel_columns    ) {
        this.name = name;
        this.columnfamilydatamodel_partitionkeys = columnfamilydatamodel_partitionkeys;
        this.columnfamilydatamodel_clusteringkeys = columnfamilydatamodel_clusteringkeys;
        this.columnfamilydatamodel_columns = columnfamilydatamodel_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<columnFamilyDataModel_PartitionKey> getColumnfamilydatamodel_partitionkeys() {
        return columnfamilydatamodel_partitionkeys;
    }

    public void addColumnfamilydatamodel_partitionkey(Columnfamilydatamodel_partitionkey columnfamilydatamodel_partitionkey) {
        this.columnfamilydatamodel_partitionkeys.add(columnfamilydatamodel_partitionkey);
    }
    public List<columnFamilyDataModel_ClusteringKey> getColumnfamilydatamodel_clusteringkeys() {
        return columnfamilydatamodel_clusteringkeys;
    }

    public void addColumnfamilydatamodel_clusteringkey(Columnfamilydatamodel_clusteringkey columnfamilydatamodel_clusteringkey) {
        this.columnfamilydatamodel_clusteringkeys.add(columnfamilydatamodel_clusteringkey);
    }
    public List<columnFamilyDataModel_Column> getColumnfamilydatamodel_columns() {
        return columnfamilydatamodel_columns;
    }

    public void addColumnfamilydatamodel_column(Columnfamilydatamodel_column columnfamilydatamodel_column) {
        this.columnfamilydatamodel_columns.add(columnfamilydatamodel_column);
    }
    public columnFamilyDataModel_ColumnFamilyDataModel getColumnfamilydatamodel_columnfamilydatamodel() {
        return columnfamilydatamodel_columnfamilydatamodel;
    }

    public void setColumnfamilydatamodel_columnfamilydatamodel(columnFamilyDataModel_ColumnFamilyDataModel columnfamilydatamodel_columnfamilydatamodel) {
        this.columnfamilydatamodel_columnfamilydatamodel = columnfamilydatamodel_columnfamilydatamodel;
    }

}






import java.util.List;
import java.util.ArrayList;

public class datasetload_TableRow  {

    private int RowNumber;
    private String Key;
    private boolean NewRow;





    private datasetload_Table datasetload_table;




    private datasetload_Table datasetload_table;


    public datasetload_TableRow(
        int RowNumber,        String Key,        boolean NewRow    ) {
        this.RowNumber = RowNumber;
        this.Key = Key;
        this.NewRow = NewRow;
    }


    public int getRownumber() {
        return RowNumber;
    }

    public void setRownumber(int RowNumber) {
        this.RowNumber = RowNumber;
    }
    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
    }
    public boolean getNewrow() {
        return NewRow;
    }

    public void setNewrow(boolean NewRow) {
        this.NewRow = NewRow;
    }

    public datasetload_Table getDatasetload_table() {
        return datasetload_table;
    }

    public void setDatasetload_table(datasetload_Table datasetload_table) {
        this.datasetload_table = datasetload_table;
    }
    public datasetload_Table getDatasetload_table() {
        return datasetload_table;
    }

    public void setDatasetload_table(datasetload_Table datasetload_table) {
        this.datasetload_table = datasetload_table;
    }

}
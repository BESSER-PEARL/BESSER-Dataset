




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class datasetload_Table  {

    private String SQLStatement;
    private String ParamTableGroupAttributes;
    private String ColumnTableRowAttributes;
    private LocalDate LastLoad;
    private int NumberOfRows;
    private String Name;
    private int KeyColumns;





    private datasetload_TableGroup datasetload_tablegroup;




    private datasetload_TableGroup datasetload_tablegroup;


    public datasetload_Table(
        String SQLStatement,        String ParamTableGroupAttributes,        String ColumnTableRowAttributes,        LocalDate LastLoad,        int NumberOfRows,        String Name,        int KeyColumns    ) {
        this.SQLStatement = SQLStatement;
        this.ParamTableGroupAttributes = ParamTableGroupAttributes;
        this.ColumnTableRowAttributes = ColumnTableRowAttributes;
        this.LastLoad = LastLoad;
        this.NumberOfRows = NumberOfRows;
        this.Name = Name;
        this.KeyColumns = KeyColumns;
    }


    public String getSqlstatement() {
        return SQLStatement;
    }

    public void setSqlstatement(String SQLStatement) {
        this.SQLStatement = SQLStatement;
    }
    public String getParamtablegroupattributes() {
        return ParamTableGroupAttributes;
    }

    public void setParamtablegroupattributes(String ParamTableGroupAttributes) {
        this.ParamTableGroupAttributes = ParamTableGroupAttributes;
    }
    public String getColumntablerowattributes() {
        return ColumnTableRowAttributes;
    }

    public void setColumntablerowattributes(String ColumnTableRowAttributes) {
        this.ColumnTableRowAttributes = ColumnTableRowAttributes;
    }
    public LocalDate getLastload() {
        return LastLoad;
    }

    public void setLastload(LocalDate LastLoad) {
        this.LastLoad = LastLoad;
    }
    public int getNumberofrows() {
        return NumberOfRows;
    }

    public void setNumberofrows(int NumberOfRows) {
        this.NumberOfRows = NumberOfRows;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getKeycolumns() {
        return KeyColumns;
    }

    public void setKeycolumns(int KeyColumns) {
        this.KeyColumns = KeyColumns;
    }

    public datasetload_TableGroup getDatasetload_tablegroup() {
        return datasetload_tablegroup;
    }

    public void setDatasetload_tablegroup(datasetload_TableGroup datasetload_tablegroup) {
        this.datasetload_tablegroup = datasetload_tablegroup;
    }
    public datasetload_TableGroup getDatasetload_tablegroup() {
        return datasetload_tablegroup;
    }

    public void setDatasetload_tablegroup(datasetload_TableGroup datasetload_tablegroup) {
        this.datasetload_tablegroup = datasetload_tablegroup;
    }

}
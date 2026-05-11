





import java.util.List;
import java.util.ArrayList;

public class nosql_Column  {

    private String datatype;
    private String name;
    private String size;





    private nosql_PK nosql_pk;




    private nosql_Index nosql_index;




    private nosql_ColumnFamily nosql_columnfamily;




    private nosql_ColumnFamily nosql_columnfamily;


    public nosql_Column(
        String datatype,        String name,        String size    ) {
        this.datatype = datatype;
        this.name = name;
        this.size = size;
    }


    public String getDatatype() {
        return datatype;
    }

    public void setDatatype(String datatype) {
        this.datatype = datatype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public nosql_PK getNosql_pk() {
        return nosql_pk;
    }

    public void setNosql_pk(nosql_PK nosql_pk) {
        this.nosql_pk = nosql_pk;
    }
    public nosql_Index getNosql_index() {
        return nosql_index;
    }

    public void setNosql_index(nosql_Index nosql_index) {
        this.nosql_index = nosql_index;
    }
    public nosql_ColumnFamily getNosql_columnfamily() {
        return nosql_columnfamily;
    }

    public void setNosql_columnfamily(nosql_ColumnFamily nosql_columnfamily) {
        this.nosql_columnfamily = nosql_columnfamily;
    }
    public nosql_ColumnFamily getNosql_columnfamily() {
        return nosql_columnfamily;
    }

    public void setNosql_columnfamily(nosql_ColumnFamily nosql_columnfamily) {
        this.nosql_columnfamily = nosql_columnfamily;
    }

}
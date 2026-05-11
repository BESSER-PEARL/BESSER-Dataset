





import java.util.List;
import java.util.ArrayList;

public class DDL_CreateCk  {

    private String nameCk;
    private String columnName;
    private String valuesCk;





    private DDL_CreateTable ddl_createtable;


    public DDL_CreateCk(
        String nameCk,        String columnName,        String valuesCk    ) {
        this.nameCk = nameCk;
        this.columnName = columnName;
        this.valuesCk = valuesCk;
    }


    public String getNameck() {
        return nameCk;
    }

    public void setNameck(String nameCk) {
        this.nameCk = nameCk;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getValuesck() {
        return valuesCk;
    }

    public void setValuesck(String valuesCk) {
        this.valuesCk = valuesCk;
    }

    public DDL_CreateTable getDdl_createtable() {
        return ddl_createtable;
    }

    public void setDdl_createtable(DDL_CreateTable ddl_createtable) {
        this.ddl_createtable = ddl_createtable;
    }

}
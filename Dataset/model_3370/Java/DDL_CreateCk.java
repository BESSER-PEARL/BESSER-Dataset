





import java.util.List;
import java.util.ArrayList;

public class DDL_CreateCk  {

    private String valuesCk;
    private String nameCk;
    private String nameColumn;





    private DDL_CreateTable ddl_createtable;


    public DDL_CreateCk(
        String valuesCk,        String nameCk,        String nameColumn    ) {
        this.valuesCk = valuesCk;
        this.nameCk = nameCk;
        this.nameColumn = nameColumn;
    }


    public String getValuesck() {
        return valuesCk;
    }

    public void setValuesck(String valuesCk) {
        this.valuesCk = valuesCk;
    }
    public String getNameck() {
        return nameCk;
    }

    public void setNameck(String nameCk) {
        this.nameCk = nameCk;
    }
    public String getNamecolumn() {
        return nameColumn;
    }

    public void setNamecolumn(String nameColumn) {
        this.nameColumn = nameColumn;
    }

    public DDL_CreateTable getDdl_createtable() {
        return ddl_createtable;
    }

    public void setDdl_createtable(DDL_CreateTable ddl_createtable) {
        this.ddl_createtable = ddl_createtable;
    }

}
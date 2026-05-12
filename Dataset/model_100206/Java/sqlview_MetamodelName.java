





import java.util.List;
import java.util.ArrayList;

public class sqlview_MetamodelName  {

    private String name;





    private sqlview_SelectAttribute sqlview_selectattribute;




    private sqlview_Metamodel sqlview_metamodel;


    public sqlview_MetamodelName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqlview_SelectAttribute getSqlview_selectattribute() {
        return sqlview_selectattribute;
    }

    public void setSqlview_selectattribute(sqlview_SelectAttribute sqlview_selectattribute) {
        this.sqlview_selectattribute = sqlview_selectattribute;
    }
    public sqlview_Metamodel getSqlview_metamodel() {
        return sqlview_metamodel;
    }

    public void setSqlview_metamodel(sqlview_Metamodel sqlview_metamodel) {
        this.sqlview_metamodel = sqlview_metamodel;
    }

}
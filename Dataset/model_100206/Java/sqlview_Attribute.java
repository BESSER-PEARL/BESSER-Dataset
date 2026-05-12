





import java.util.List;
import java.util.ArrayList;

public class sqlview_Attribute  {

    private String name;





    private sqlview_SelectAttribute sqlview_selectattribute;


    public sqlview_Attribute(
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

}
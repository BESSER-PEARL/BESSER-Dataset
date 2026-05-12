





import java.util.List;
import java.util.ArrayList;

public class sqlview_Class  {

    private String name;





    private sqlview_JoinLeft sqlview_joinleft;




    private sqlview_SelectAttribute sqlview_selectattribute;




    private sqlview_JoinRight sqlview_joinright;


    public sqlview_Class(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqlview_JoinLeft getSqlview_joinleft() {
        return sqlview_joinleft;
    }

    public void setSqlview_joinleft(sqlview_JoinLeft sqlview_joinleft) {
        this.sqlview_joinleft = sqlview_joinleft;
    }
    public sqlview_SelectAttribute getSqlview_selectattribute() {
        return sqlview_selectattribute;
    }

    public void setSqlview_selectattribute(sqlview_SelectAttribute sqlview_selectattribute) {
        this.sqlview_selectattribute = sqlview_selectattribute;
    }
    public sqlview_JoinRight getSqlview_joinright() {
        return sqlview_joinright;
    }

    public void setSqlview_joinright(sqlview_JoinRight sqlview_joinright) {
        this.sqlview_joinright = sqlview_joinright;
    }

}
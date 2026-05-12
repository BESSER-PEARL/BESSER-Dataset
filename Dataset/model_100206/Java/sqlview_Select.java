





import java.util.List;
import java.util.ArrayList;

public class sqlview_Select  {

    private String select;





    private sqlview_Expression sqlview_expression;




    private List<sqlview_SelectAttribute> sqlview_selectattributes;


    public sqlview_Select(
        String select    ) {
        this.select = select;
        this.sqlview_selectattributes = new ArrayList<>();
    }

    public sqlview_Select(
        String select        ArrayList<sqlview_SelectAttribute> sqlview_selectattributes    ) {
        this.select = select;
        this.sqlview_selectattributes = sqlview_selectattributes;
    }

    public String getSelect() {
        return select;
    }

    public void setSelect(String select) {
        this.select = select;
    }

    public sqlview_Expression getSqlview_expression() {
        return sqlview_expression;
    }

    public void setSqlview_expression(sqlview_Expression sqlview_expression) {
        this.sqlview_expression = sqlview_expression;
    }
    public List<sqlview_SelectAttribute> getSqlview_selectattributes() {
        return sqlview_selectattributes;
    }

    public void addSqlview_selectattribute(Sqlview_selectattribute sqlview_selectattribute) {
        this.sqlview_selectattributes.add(sqlview_selectattribute);
    }

}
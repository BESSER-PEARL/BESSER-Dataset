





import java.util.List;
import java.util.ArrayList;

public class d3ql_PathElement  {

    private String name;





    private d3ql_PathExpression d3ql_pathexpression;


    public d3ql_PathElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public d3ql_PathExpression getD3ql_pathexpression() {
        return d3ql_pathexpression;
    }

    public void setD3ql_pathexpression(d3ql_PathExpression d3ql_pathexpression) {
        this.d3ql_pathexpression = d3ql_pathexpression;
    }

}
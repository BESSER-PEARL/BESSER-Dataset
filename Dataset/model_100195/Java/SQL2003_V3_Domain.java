





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_Domain  {

    private String name;
    private String expression;
    private String default;





    private SQL2003_V3_Schema sql2003_v3_schema;




    private SQL2003_V3_Schema sql2003_v3_schema;


    public SQL2003_V3_Domain(
        String name,        String expression,        String default    ) {
        this.name = name;
        this.expression = expression;
        this.default = default;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public SQL2003_V3_Schema getSql2003_v3_schema() {
        return sql2003_v3_schema;
    }

    public void setSql2003_v3_schema(SQL2003_V3_Schema sql2003_v3_schema) {
        this.sql2003_v3_schema = sql2003_v3_schema;
    }
    public SQL2003_V3_Schema getSql2003_v3_schema() {
        return sql2003_v3_schema;
    }

    public void setSql2003_v3_schema(SQL2003_V3_Schema sql2003_v3_schema) {
        this.sql2003_v3_schema = sql2003_v3_schema;
    }

}
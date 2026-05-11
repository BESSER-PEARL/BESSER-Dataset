





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CastExpression extends Expression {

    private String type;





    private sqliteModel_Expression sqlitemodel_expression;


    public sqliteModel_CastExpression(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }

}
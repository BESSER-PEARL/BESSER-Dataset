





import java.util.List;
import java.util.ArrayList;

public class plsql_expression_PropertyAccess extends Expression {

    private String propertyName;



    public plsql_expression_PropertyAccess(
        String propertyName    ) {
        super(
        );
        this.propertyName = propertyName;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }


}
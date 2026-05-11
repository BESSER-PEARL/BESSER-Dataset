





import java.util.List;
import java.util.ArrayList;

public class majordomo_PreparedStatement  {

    private String name;





    private majordomo_StatementReference majordomo_statementreference;


    public majordomo_PreparedStatement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public majordomo_StatementReference getMajordomo_statementreference() {
        return majordomo_statementreference;
    }

    public void setMajordomo_statementreference(majordomo_StatementReference majordomo_statementreference) {
        this.majordomo_statementreference = majordomo_statementreference;
    }

}
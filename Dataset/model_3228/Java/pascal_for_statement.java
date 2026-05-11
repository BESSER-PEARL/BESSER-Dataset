





import java.util.List;
import java.util.ArrayList;

public class pascal_for_statement  {

    private String initID;





    private pascal_statement pascal_statement;


    public pascal_for_statement(
        String initID    ) {
        this.initID = initID;
    }


    public String getInitid() {
        return initID;
    }

    public void setInitid(String initID) {
        this.initID = initID;
    }

    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }

}
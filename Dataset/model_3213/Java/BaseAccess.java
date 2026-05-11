





import java.util.List;
import java.util.ArrayList;

public class BaseAccess  {






    private gast_statements_Statement gast_statements_statement;




    private gast_accesses_CompositeAccess gast_accesses_compositeaccess;


    public BaseAccess(
    ) {
    }



    public gast_statements_Statement getGast_statements_statement() {
        return gast_statements_statement;
    }

    public void setGast_statements_statement(gast_statements_Statement gast_statements_statement) {
        this.gast_statements_statement = gast_statements_statement;
    }
    public gast_accesses_CompositeAccess getGast_accesses_compositeaccess() {
        return gast_accesses_compositeaccess;
    }

    public void setGast_accesses_compositeaccess(gast_accesses_CompositeAccess gast_accesses_compositeaccess) {
        this.gast_accesses_compositeaccess = gast_accesses_compositeaccess;
    }

}
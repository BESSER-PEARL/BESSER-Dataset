





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Variable  {

    private String name;





    private mMDSL_Variable mmdsl_variable;




    private mMDSL_Statement mmdsl_statement;


    public mMDSL_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_Variable getMmdsl_variable() {
        return mmdsl_variable;
    }

    public void setMmdsl_variable(mMDSL_Variable mmdsl_variable) {
        this.mmdsl_variable = mmdsl_variable;
    }
    public mMDSL_Statement getMmdsl_statement() {
        return mmdsl_statement;
    }

    public void setMmdsl_statement(mMDSL_Statement mmdsl_statement) {
        this.mmdsl_statement = mmdsl_statement;
    }

}
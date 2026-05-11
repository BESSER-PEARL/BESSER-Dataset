





import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeSwitchCase  {

    private String case;
    private String default;





    private myDsl_TypeCaseClause mydsl_typecaseclause;


    public myDsl_TypeSwitchCase(
        String case,        String default    ) {
        this.case = case;
        this.default = default;
    }


    public String getCase() {
        return case;
    }

    public void setCase(String case) {
        this.case = case;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public myDsl_TypeCaseClause getMydsl_typecaseclause() {
        return mydsl_typecaseclause;
    }

    public void setMydsl_typecaseclause(myDsl_TypeCaseClause mydsl_typecaseclause) {
        this.mydsl_typecaseclause = mydsl_typecaseclause;
    }

}
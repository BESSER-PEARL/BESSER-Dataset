





import java.util.List;
import java.util.ArrayList;

public class pivot_VariableExp extends OCLExpression, ReferringElement {

    private String implicit;



    public pivot_VariableExp(
        String implicit    ) {
        super(
        );
        this.implicit = implicit;
    }


    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
    }


}
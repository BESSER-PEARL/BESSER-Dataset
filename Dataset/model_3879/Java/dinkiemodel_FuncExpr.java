





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_FuncExpr extends Expression, Statement {

    private String funcName;



    public dinkiemodel_FuncExpr(
        String funcName    ) {
        super(
        );
        this.funcName = funcName;
    }


    public String getFuncname() {
        return funcName;
    }

    public void setFuncname(String funcName) {
        this.funcName = funcName;
    }


}
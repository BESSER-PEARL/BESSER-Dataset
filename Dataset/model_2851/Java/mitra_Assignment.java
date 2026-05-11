





import java.util.List;
import java.util.ArrayList;

public class mitra_Assignment extends StatementExpression {

    private String operator;





    private List<mitra_VariableAccess> mitra_variableaccesss;




    private mitra_Expression mitra_expression;


    public mitra_Assignment(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.mitra_variableaccesss = new ArrayList<>();
    }

    public mitra_Assignment(
        String operator        ArrayList<mitra_VariableAccess> mitra_variableaccesss    ) {
        this.operator = operator;
        this.mitra_variableaccesss = mitra_variableaccesss;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<mitra_VariableAccess> getMitra_variableaccesss() {
        return mitra_variableaccesss;
    }

    public void addMitra_variableaccess(Mitra_variableaccess mitra_variableaccess) {
        this.mitra_variableaccesss.add(mitra_variableaccess);
    }
    public mitra_Expression getMitra_expression() {
        return mitra_expression;
    }

    public void setMitra_expression(mitra_Expression mitra_expression) {
        this.mitra_expression = mitra_expression;
    }

}
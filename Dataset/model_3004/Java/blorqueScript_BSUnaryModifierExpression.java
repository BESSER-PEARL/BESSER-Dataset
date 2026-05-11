





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSUnaryModifierExpression extends BSExpression {

    private String operator;





    private blorqueScript_BSExpression blorquescript_bsexpression;


    public blorqueScript_BSUnaryModifierExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public blorqueScript_BSExpression getBlorquescript_bsexpression() {
        return blorquescript_bsexpression;
    }

    public void setBlorquescript_bsexpression(blorqueScript_BSExpression blorquescript_bsexpression) {
        this.blorquescript_bsexpression = blorquescript_bsexpression;
    }

}
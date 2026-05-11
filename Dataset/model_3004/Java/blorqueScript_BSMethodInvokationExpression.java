





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSMethodInvokationExpression extends BSExpression {






    private blorqueScript_BSExpression blorquescript_bsexpression;




    private List<blorqueScript_BSExpression> blorquescript_bsexpressions;


    public blorqueScript_BSMethodInvokationExpression(
    ) {
        super(
        );
        this.blorquescript_bsexpressions = new ArrayList<>();
    }

    public blorqueScript_BSMethodInvokationExpression(
        ArrayList<blorqueScript_BSExpression> blorquescript_bsexpressions    ) {
        this.blorquescript_bsexpressions = blorquescript_bsexpressions;
    }


    public blorqueScript_BSExpression getBlorquescript_bsexpression() {
        return blorquescript_bsexpression;
    }

    public void setBlorquescript_bsexpression(blorqueScript_BSExpression blorquescript_bsexpression) {
        this.blorquescript_bsexpression = blorquescript_bsexpression;
    }
    public List<blorqueScript_BSExpression> getBlorquescript_bsexpressions() {
        return blorquescript_bsexpressions;
    }

    public void addBlorquescript_bsexpression(Blorquescript_bsexpression blorquescript_bsexpression) {
        this.blorquescript_bsexpressions.add(blorquescript_bsexpression);
    }

}
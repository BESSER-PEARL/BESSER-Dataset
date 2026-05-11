





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSNewExpression extends BSExpression {

    private boolean isArray;





    private List<blorqueScript_BSExpression> blorquescript_bsexpressions;




    private blorqueScript_BSClass blorquescript_bsclass;


    public blorqueScript_BSNewExpression(
        boolean isArray    ) {
        super(
        );
        this.isArray = isArray;
        this.blorquescript_bsexpressions = new ArrayList<>();
    }

    public blorqueScript_BSNewExpression(
        boolean isArray        ArrayList<blorqueScript_BSExpression> blorquescript_bsexpressions    ) {
        this.isArray = isArray;
        this.blorquescript_bsexpressions = blorquescript_bsexpressions;
    }

    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }

    public List<blorqueScript_BSExpression> getBlorquescript_bsexpressions() {
        return blorquescript_bsexpressions;
    }

    public void addBlorquescript_bsexpression(Blorquescript_bsexpression blorquescript_bsexpression) {
        this.blorquescript_bsexpressions.add(blorquescript_bsexpression);
    }
    public blorqueScript_BSClass getBlorquescript_bsclass() {
        return blorquescript_bsclass;
    }

    public void setBlorquescript_bsclass(blorqueScript_BSClass blorquescript_bsclass) {
        this.blorquescript_bsclass = blorquescript_bsclass;
    }

}






import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSCastExpression extends BSExpression {

    private boolean isArray;
    private String pType;





    private blorqueScript_BSExpression blorquescript_bsexpression;


    public blorqueScript_BSCastExpression(
        boolean isArray,        String pType    ) {
        super(
        );
        this.isArray = isArray;
        this.pType = pType;
    }


    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }
    public String getPtype() {
        return pType;
    }

    public void setPtype(String pType) {
        this.pType = pType;
    }

    public blorqueScript_BSExpression getBlorquescript_bsexpression() {
        return blorquescript_bsexpression;
    }

    public void setBlorquescript_bsexpression(blorqueScript_BSExpression blorquescript_bsexpression) {
        this.blorquescript_bsexpression = blorquescript_bsexpression;
    }

}
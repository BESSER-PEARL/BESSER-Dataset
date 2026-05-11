





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSRealConstant extends BSExpression {

    private int right;





    private blorqueScript_BSNumberConstant blorquescript_bsnumberconstant;


    public blorqueScript_BSRealConstant(
        int right    ) {
        super(
        );
        this.right = right;
    }


    public int getRight() {
        return right;
    }

    public void setRight(int right) {
        this.right = right;
    }

    public blorqueScript_BSNumberConstant getBlorquescript_bsnumberconstant() {
        return blorquescript_bsnumberconstant;
    }

    public void setBlorquescript_bsnumberconstant(blorqueScript_BSNumberConstant blorquescript_bsnumberconstant) {
        this.blorquescript_bsnumberconstant = blorquescript_bsnumberconstant;
    }

}
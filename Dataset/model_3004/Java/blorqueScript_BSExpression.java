





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSExpression extends BSStatement {






    private blorqueScript_BSVariableDeclaration blorquescript_bsvariabledeclaration;




    private blorqueScript_BSReturn blorquescript_bsreturn;




    private blorqueScript_BSIfStatement blorquescript_bsifstatement;


    public blorqueScript_BSExpression(
    ) {
        super(
        );
    }



    public blorqueScript_BSVariableDeclaration getBlorquescript_bsvariabledeclaration() {
        return blorquescript_bsvariabledeclaration;
    }

    public void setBlorquescript_bsvariabledeclaration(blorqueScript_BSVariableDeclaration blorquescript_bsvariabledeclaration) {
        this.blorquescript_bsvariabledeclaration = blorquescript_bsvariabledeclaration;
    }
    public blorqueScript_BSReturn getBlorquescript_bsreturn() {
        return blorquescript_bsreturn;
    }

    public void setBlorquescript_bsreturn(blorqueScript_BSReturn blorquescript_bsreturn) {
        this.blorquescript_bsreturn = blorquescript_bsreturn;
    }
    public blorqueScript_BSIfStatement getBlorquescript_bsifstatement() {
        return blorquescript_bsifstatement;
    }

    public void setBlorquescript_bsifstatement(blorqueScript_BSIfStatement blorquescript_bsifstatement) {
        this.blorquescript_bsifstatement = blorquescript_bsifstatement;
    }

}
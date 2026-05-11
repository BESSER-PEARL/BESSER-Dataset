





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSSwitchStatement extends BSStatement {

    private boolean stringSwitch;





    private blorqueScript_BSSwitchBlock blorquescript_bsswitchblock;




    private blorqueScript_BSExpression blorquescript_bsexpression;


    public blorqueScript_BSSwitchStatement(
        boolean stringSwitch    ) {
        super(
        );
        this.stringSwitch = stringSwitch;
    }


    public boolean getStringswitch() {
        return stringSwitch;
    }

    public void setStringswitch(boolean stringSwitch) {
        this.stringSwitch = stringSwitch;
    }

    public blorqueScript_BSSwitchBlock getBlorquescript_bsswitchblock() {
        return blorquescript_bsswitchblock;
    }

    public void setBlorquescript_bsswitchblock(blorqueScript_BSSwitchBlock blorquescript_bsswitchblock) {
        this.blorquescript_bsswitchblock = blorquescript_bsswitchblock;
    }
    public blorqueScript_BSExpression getBlorquescript_bsexpression() {
        return blorquescript_bsexpression;
    }

    public void setBlorquescript_bsexpression(blorqueScript_BSExpression blorquescript_bsexpression) {
        this.blorquescript_bsexpression = blorquescript_bsexpression;
    }

}
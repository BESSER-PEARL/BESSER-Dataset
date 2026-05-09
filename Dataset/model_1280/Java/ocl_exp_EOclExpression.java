





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_EOclExpression  {






    private ELoopExp eloopexp;




    private ENavigationCallExp enavigationcallexp;




    private ECallExp ecallexp;




    private EVariable evariable;


    public ocl_exp_EOclExpression(
    ) {
    }



    public ELoopExp getEloopexp() {
        return eloopexp;
    }

    public void setEloopexp(ELoopExp eloopexp) {
        this.eloopexp = eloopexp;
    }
    public ENavigationCallExp getEnavigationcallexp() {
        return enavigationcallexp;
    }

    public void setEnavigationcallexp(ENavigationCallExp enavigationcallexp) {
        this.enavigationcallexp = enavigationcallexp;
    }
    public ECallExp getEcallexp() {
        return ecallexp;
    }

    public void setEcallexp(ECallExp ecallexp) {
        this.ecallexp = ecallexp;
    }
    public EVariable getEvariable() {
        return evariable;
    }

    public void setEvariable(EVariable evariable) {
        this.evariable = evariable;
    }

}
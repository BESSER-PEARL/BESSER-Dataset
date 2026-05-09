





import java.util.List;
import java.util.ArrayList;

public class shadowrun_AbstrakteRuestung extends AbstraktKleidung {

    private int ruestungsSchutzBalistisch;
    private int ruestungsSchutzStoss;



    public shadowrun_AbstrakteRuestung(
        int ruestungsSchutzBalistisch,        int ruestungsSchutzStoss    ) {
        super(
        );
        this.ruestungsSchutzBalistisch = ruestungsSchutzBalistisch;
        this.ruestungsSchutzStoss = ruestungsSchutzStoss;
    }


    public int getRuestungsschutzbalistisch() {
        return ruestungsSchutzBalistisch;
    }

    public void setRuestungsschutzbalistisch(int ruestungsSchutzBalistisch) {
        this.ruestungsSchutzBalistisch = ruestungsSchutzBalistisch;
    }
    public int getRuestungsschutzstoss() {
        return ruestungsSchutzStoss;
    }

    public void setRuestungsschutzstoss(int ruestungsSchutzStoss) {
        this.ruestungsSchutzStoss = ruestungsSchutzStoss;
    }


}
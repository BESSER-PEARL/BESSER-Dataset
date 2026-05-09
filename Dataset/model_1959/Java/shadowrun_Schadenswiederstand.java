





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Schadenswiederstand  {

    private int ruestungsSchutzStoss;
    private int ruestungsSchutzBalistisch;



    public shadowrun_Schadenswiederstand(
        int ruestungsSchutzStoss,        int ruestungsSchutzBalistisch    ) {
        this.ruestungsSchutzStoss = ruestungsSchutzStoss;
        this.ruestungsSchutzBalistisch = ruestungsSchutzBalistisch;
    }


    public int getRuestungsschutzstoss() {
        return ruestungsSchutzStoss;
    }

    public void setRuestungsschutzstoss(int ruestungsSchutzStoss) {
        this.ruestungsSchutzStoss = ruestungsSchutzStoss;
    }
    public int getRuestungsschutzbalistisch() {
        return ruestungsSchutzBalistisch;
    }

    public void setRuestungsschutzbalistisch(int ruestungsSchutzBalistisch) {
        this.ruestungsSchutzBalistisch = ruestungsSchutzBalistisch;
    }


}
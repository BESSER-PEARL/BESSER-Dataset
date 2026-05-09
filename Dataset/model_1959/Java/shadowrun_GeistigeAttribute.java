





import java.util.List;
import java.util.ArrayList;

public class shadowrun_GeistigeAttribute  {

    private int Charisma;
    private int Inteligenz;
    private int Willenskraft;



    public shadowrun_GeistigeAttribute(
        int Charisma,        int Inteligenz,        int Willenskraft    ) {
        this.Charisma = Charisma;
        this.Inteligenz = Inteligenz;
        this.Willenskraft = Willenskraft;
    }


    public int getCharisma() {
        return Charisma;
    }

    public void setCharisma(int Charisma) {
        this.Charisma = Charisma;
    }
    public int getInteligenz() {
        return Inteligenz;
    }

    public void setInteligenz(int Inteligenz) {
        this.Inteligenz = Inteligenz;
    }
    public int getWillenskraft() {
        return Willenskraft;
    }

    public void setWillenskraft(int Willenskraft) {
        this.Willenskraft = Willenskraft;
    }


}
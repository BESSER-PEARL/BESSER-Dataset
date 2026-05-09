





import java.util.List;
import java.util.ArrayList;

public class shr5_GeistigeAttribute extends ModifikatorAttribute {

    private int logik;
    private int intuition;
    private int charisma;
    private int willenskraft;



    public shr5_GeistigeAttribute(
        int logik,        int intuition,        int charisma,        int willenskraft    ) {
        super(
        );
        this.logik = logik;
        this.intuition = intuition;
        this.charisma = charisma;
        this.willenskraft = willenskraft;
    }


    public int getLogik() {
        return logik;
    }

    public void setLogik(int logik) {
        this.logik = logik;
    }
    public int getIntuition() {
        return intuition;
    }

    public void setIntuition(int intuition) {
        this.intuition = intuition;
    }
    public int getCharisma() {
        return charisma;
    }

    public void setCharisma(int charisma) {
        this.charisma = charisma;
    }
    public int getWillenskraft() {
        return willenskraft;
    }

    public void setWillenskraft(int willenskraft) {
        this.willenskraft = willenskraft;
    }


}
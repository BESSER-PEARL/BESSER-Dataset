





import java.util.List;
import java.util.ArrayList;

public class Attack  {

    private int requiredTokens;
    private String name;





    private List<AttackHistory> attackhistorys;


    public Attack(
        int requiredTokens,        String name    ) {
        this.requiredTokens = requiredTokens;
        this.name = name;
        this.attackhistorys = new ArrayList<>();
    }

    public Attack(
        int requiredTokens,        String name        ArrayList<AttackHistory> attackhistorys    ) {
        this.requiredTokens = requiredTokens;
        this.name = name;
        this.attackhistorys = attackhistorys;
    }

    public int getRequiredtokens() {
        return requiredTokens;
    }

    public void setRequiredtokens(int requiredTokens) {
        this.requiredTokens = requiredTokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<AttackHistory> getAttackhistorys() {
        return attackhistorys;
    }

    public void addAttackhistory(Attackhistory attackhistory) {
        this.attackhistorys.add(attackhistory);
    }

}
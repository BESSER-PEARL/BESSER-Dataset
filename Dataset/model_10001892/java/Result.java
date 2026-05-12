





import java.util.List;
import java.util.ArrayList;

public class Result  {

    private String value;





    private List<AttackHistory> attackhistorys;


    public Result(
        String value    ) {
        this.value = value;
        this.attackhistorys = new ArrayList<>();
    }

    public Result(
        String value        ArrayList<AttackHistory> attackhistorys    ) {
        this.value = value;
        this.attackhistorys = attackhistorys;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<AttackHistory> getAttackhistorys() {
        return attackhistorys;
    }

    public void addAttackhistory(Attackhistory attackhistory) {
        this.attackhistorys.add(attackhistory);
    }

}
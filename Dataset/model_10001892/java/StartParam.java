





import java.util.List;
import java.util.ArrayList;

public class StartParam  {

    private String type;
    private String value;





    private List<AttackHistory> attackhistorys;


    public StartParam(
        String type,        String value    ) {
        this.type = type;
        this.value = value;
        this.attackhistorys = new ArrayList<>();
    }

    public StartParam(
        String type,        String value        ArrayList<AttackHistory> attackhistorys    ) {
        this.type = type;
        this.value = value;
        this.attackhistorys = attackhistorys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
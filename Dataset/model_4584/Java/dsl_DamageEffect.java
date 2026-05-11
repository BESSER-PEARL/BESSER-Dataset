





import java.util.List;
import java.util.ArrayList;

public class dsl_DamageEffect extends Effect {

    private int amount;



    public dsl_DamageEffect(
        int amount    ) {
        super(
        );
        this.amount = amount;
    }


    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }


}
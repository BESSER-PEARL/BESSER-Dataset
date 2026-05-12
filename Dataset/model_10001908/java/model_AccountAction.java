





import java.util.List;
import java.util.ArrayList;

public class model_AccountAction  {

    private boolean success;
    private float amount;
    private String action;





    private List<model_Account> model_accounts;


    public model_AccountAction(
        boolean success,        float amount,        String action    ) {
        this.success = success;
        this.amount = amount;
        this.action = action;
        this.model_accounts = new ArrayList<>();
    }

    public model_AccountAction(
        boolean success,        float amount,        String action        ArrayList<model_Account> model_accounts    ) {
        this.success = success;
        this.amount = amount;
        this.action = action;
        this.model_accounts = model_accounts;
    }

    public boolean getSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public List<model_Account> getModel_accounts() {
        return model_accounts;
    }

    public void addModel_account(Model_account model_account) {
        this.model_accounts.add(model_account);
    }

}
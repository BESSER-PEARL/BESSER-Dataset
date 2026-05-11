





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_SwitchStatus  {

    private String status;





    private List<MnemonicNameReference> mnemonicnamereferences;


    public cobol_statements_SwitchStatus(
        String status    ) {
        this.status = status;
        this.mnemonicnamereferences = new ArrayList<>();
    }

    public cobol_statements_SwitchStatus(
        String status        ArrayList<MnemonicNameReference> mnemonicnamereferences    ) {
        this.status = status;
        this.mnemonicnamereferences = mnemonicnamereferences;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<MnemonicNameReference> getMnemonicnamereferences() {
        return mnemonicnamereferences;
    }

    public void addMnemonicnamereference(Mnemonicnamereference mnemonicnamereference) {
        this.mnemonicnamereferences.add(mnemonicnamereference);
    }

}
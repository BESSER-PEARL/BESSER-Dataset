





import java.util.List;
import java.util.ArrayList;

public class fsa_State  {

    private String name;
    private boolean accepting;





    private fsa_FSA fsa_fsa;




    private fsa_FSA fsa_fsa;


    public fsa_State(
        String name,        boolean accepting    ) {
        this.name = name;
        this.accepting = accepting;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getAccepting() {
        return accepting;
    }

    public void setAccepting(boolean accepting) {
        this.accepting = accepting;
    }

    public fsa_FSA getFsa_fsa() {
        return fsa_fsa;
    }

    public void setFsa_fsa(fsa_FSA fsa_fsa) {
        this.fsa_fsa = fsa_fsa;
    }
    public fsa_FSA getFsa_fsa() {
        return fsa_fsa;
    }

    public void setFsa_fsa(fsa_FSA fsa_fsa) {
        this.fsa_fsa = fsa_fsa;
    }

}
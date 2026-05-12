





import java.util.List;
import java.util.ArrayList;

public class mmb_Automaton  {

    private String Name;





    private mmb_Model mmb_model;


    public mmb_Automaton(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public mmb_Model getMmb_model() {
        return mmb_model;
    }

    public void setMmb_model(mmb_Model mmb_model) {
        this.mmb_model = mmb_model;
    }

}
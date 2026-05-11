





import java.util.List;
import java.util.ArrayList;

public class iot2_Input  {






    private List<iot2_InputValue> iot2_inputvalues;


    public iot2_Input(
    ) {
        this.iot2_inputvalues = new ArrayList<>();
    }

    public iot2_Input(
        ArrayList<iot2_InputValue> iot2_inputvalues    ) {
        this.iot2_inputvalues = iot2_inputvalues;
    }


    public List<iot2_InputValue> getIot2_inputvalues() {
        return iot2_inputvalues;
    }

    public void addIot2_inputvalue(Iot2_inputvalue iot2_inputvalue) {
        this.iot2_inputvalues.add(iot2_inputvalue);
    }

}
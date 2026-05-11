





import java.util.List;
import java.util.ArrayList;

public class iot2_Context  {






    private List<iot2_InputValue> iot2_inputvalues;




    private iot2_Context iot2_context;




    private iot2_JoinNode iot2_joinnode;


    public iot2_Context(
    ) {
        this.iot2_inputvalues = new ArrayList<>();
    }

    public iot2_Context(
        ArrayList<iot2_InputValue> iot2_inputvalues    ) {
        this.iot2_inputvalues = iot2_inputvalues;
    }


    public List<iot2_InputValue> getIot2_inputvalues() {
        return iot2_inputvalues;
    }

    public void addIot2_inputvalue(Iot2_inputvalue iot2_inputvalue) {
        this.iot2_inputvalues.add(iot2_inputvalue);
    }
    public iot2_Context getIot2_context() {
        return iot2_context;
    }

    public void setIot2_context(iot2_Context iot2_context) {
        this.iot2_context = iot2_context;
    }
    public iot2_JoinNode getIot2_joinnode() {
        return iot2_joinnode;
    }

    public void setIot2_joinnode(iot2_JoinNode iot2_joinnode) {
        this.iot2_joinnode = iot2_joinnode;
    }

}
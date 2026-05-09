





import java.util.List;
import java.util.ArrayList;

public class cjsidl_nextState  {

    private String comment;





    private cjsidl_state cjsidl_state;




    private cjsidl_state cjsidl_state;




    private List<cjsidl_state> cjsidl_states;


    public cjsidl_nextState(
        String comment    ) {
        this.comment = comment;
        this.cjsidl_states = new ArrayList<>();
    }

    public cjsidl_nextState(
        String comment        ArrayList<cjsidl_state> cjsidl_states    ) {
        this.comment = comment;
        this.cjsidl_states = cjsidl_states;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_state getCjsidl_state() {
        return cjsidl_state;
    }

    public void setCjsidl_state(cjsidl_state cjsidl_state) {
        this.cjsidl_state = cjsidl_state;
    }
    public cjsidl_state getCjsidl_state() {
        return cjsidl_state;
    }

    public void setCjsidl_state(cjsidl_state cjsidl_state) {
        this.cjsidl_state = cjsidl_state;
    }
    public List<cjsidl_state> getCjsidl_states() {
        return cjsidl_states;
    }

    public void addCjsidl_state(Cjsidl_state cjsidl_state) {
        this.cjsidl_states.add(cjsidl_state);
    }

}
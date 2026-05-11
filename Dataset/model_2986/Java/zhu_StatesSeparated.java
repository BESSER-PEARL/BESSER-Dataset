





import java.util.List;
import java.util.ArrayList;

public class zhu_StatesSeparated  {






    private List<zhu_State> zhu_states;




    private zhu_State zhu_state;




    private zhu_States zhu_states;


    public zhu_StatesSeparated(
    ) {
        this.zhu_states = new ArrayList<>();
    }

    public zhu_StatesSeparated(
        ArrayList<zhu_State> zhu_states    ) {
        this.zhu_states = zhu_states;
    }


    public List<zhu_State> getZhu_states() {
        return zhu_states;
    }

    public void addZhu_state(Zhu_state zhu_state) {
        this.zhu_states.add(zhu_state);
    }
    public zhu_State getZhu_state() {
        return zhu_state;
    }

    public void setZhu_state(zhu_State zhu_state) {
        this.zhu_state = zhu_state;
    }
    public zhu_States getZhu_states() {
        return zhu_states;
    }

    public void setZhu_states(zhu_States zhu_states) {
        this.zhu_states = zhu_states;
    }

}
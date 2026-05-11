





import java.util.List;
import java.util.ArrayList;

public class df_FSM extends Graph {






    private df_State df_state;




    private df_Actor df_actor;


    public df_FSM(
    ) {
        super(
        );
    }



    public df_State getDf_state() {
        return df_state;
    }

    public void setDf_state(df_State df_state) {
        this.df_state = df_state;
    }
    public df_Actor getDf_actor() {
        return df_actor;
    }

    public void setDf_actor(df_Actor df_actor) {
        this.df_actor = df_actor;
    }

}
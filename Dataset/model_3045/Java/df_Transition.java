





import java.util.List;
import java.util.ArrayList;

public class df_Transition extends Edge {






    private List<df_Action> df_actions;


    public df_Transition(
    ) {
        super(
        );
        this.df_actions = new ArrayList<>();
    }

    public df_Transition(
        ArrayList<df_Action> df_actions    ) {
        this.df_actions = df_actions;
    }


    public List<df_Action> getDf_actions() {
        return df_actions;
    }

    public void addDf_action(Df_action df_action) {
        this.df_actions.add(df_action);
    }

}
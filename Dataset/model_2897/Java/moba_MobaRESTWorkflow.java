





import java.util.List;
import java.util.ArrayList;

public class moba_MobaRESTWorkflow extends MobaREST {






    private moba_MobaRESTWorkflow moba_mobarestworkflow;




    private List<moba_MobaREST> moba_mobarests;


    public moba_MobaRESTWorkflow(
    ) {
        super(
        );
        this.moba_mobarests = new ArrayList<>();
    }

    public moba_MobaRESTWorkflow(
        ArrayList<moba_MobaREST> moba_mobarests    ) {
        this.moba_mobarests = moba_mobarests;
    }


    public moba_MobaRESTWorkflow getMoba_mobarestworkflow() {
        return moba_mobarestworkflow;
    }

    public void setMoba_mobarestworkflow(moba_MobaRESTWorkflow moba_mobarestworkflow) {
        this.moba_mobarestworkflow = moba_mobarestworkflow;
    }
    public List<moba_MobaREST> getMoba_mobarests() {
        return moba_mobarests;
    }

    public void addMoba_mobarest(Moba_mobarest moba_mobarest) {
        this.moba_mobarests.add(moba_mobarest);
    }

}






import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_LinkAction extends Action {






    private List<CompleteDSLPckg_InputPin> completedslpckg_inputpins;




    private List<CompleteDSLPckg_LinkEndData> completedslpckg_linkenddatas;


    public CompleteDSLPckg_LinkAction(
    ) {
        super(
        );
        this.completedslpckg_inputpins = new ArrayList<>();
        this.completedslpckg_linkenddatas = new ArrayList<>();
    }

    public CompleteDSLPckg_LinkAction(
        ArrayList<CompleteDSLPckg_InputPin> completedslpckg_inputpins,        ArrayList<CompleteDSLPckg_LinkEndData> completedslpckg_linkenddatas    ) {
        this.completedslpckg_inputpins = completedslpckg_inputpins;
        this.completedslpckg_linkenddatas = completedslpckg_linkenddatas;
    }


    public List<CompleteDSLPckg_InputPin> getCompletedslpckg_inputpins() {
        return completedslpckg_inputpins;
    }

    public void addCompletedslpckg_inputpin(Completedslpckg_inputpin completedslpckg_inputpin) {
        this.completedslpckg_inputpins.add(completedslpckg_inputpin);
    }
    public List<CompleteDSLPckg_LinkEndData> getCompletedslpckg_linkenddatas() {
        return completedslpckg_linkenddatas;
    }

    public void addCompletedslpckg_linkenddata(Completedslpckg_linkenddata completedslpckg_linkenddata) {
        this.completedslpckg_linkenddatas.add(completedslpckg_linkenddata);
    }

}
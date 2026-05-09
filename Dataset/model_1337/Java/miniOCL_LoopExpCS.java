





import java.util.List;
import java.util.ArrayList;

public class miniOCL_LoopExpCS extends NavigationExpCS {

    private String logicOp;





    private List<miniOCL_ExpCS> miniocl_expcss;


    public miniOCL_LoopExpCS(
        String logicOp    ) {
        super(
        );
        this.logicOp = logicOp;
        this.miniocl_expcss = new ArrayList<>();
    }

    public miniOCL_LoopExpCS(
        String logicOp        ArrayList<miniOCL_ExpCS> miniocl_expcss    ) {
        this.logicOp = logicOp;
        this.miniocl_expcss = miniocl_expcss;
    }

    public String getLogicop() {
        return logicOp;
    }

    public void setLogicop(String logicOp) {
        this.logicOp = logicOp;
    }

    public List<miniOCL_ExpCS> getMiniocl_expcss() {
        return miniocl_expcss;
    }

    public void addMiniocl_expcs(Miniocl_expcs miniocl_expcs) {
        this.miniocl_expcss.add(miniocl_expcs);
    }

}
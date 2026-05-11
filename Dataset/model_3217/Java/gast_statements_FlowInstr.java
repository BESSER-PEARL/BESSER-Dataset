





import java.util.List;
import java.util.ArrayList;

public class gast_statements_FlowInstr  {

    private String txt;





    private List<FlowInstr> flowinstrs;




    private List<FlowInstr> flowinstrs;


    public gast_statements_FlowInstr(
        String txt    ) {
        this.txt = txt;
        this.flowinstrs = new ArrayList<>();
        this.flowinstrs = new ArrayList<>();
    }

    public gast_statements_FlowInstr(
        String txt        ArrayList<FlowInstr> flowinstrs,        ArrayList<FlowInstr> flowinstrs    ) {
        this.txt = txt;
        this.flowinstrs = flowinstrs;
        this.flowinstrs = flowinstrs;
    }

    public String getTxt() {
        return txt;
    }

    public void setTxt(String txt) {
        this.txt = txt;
    }

    public List<FlowInstr> getFlowinstrs() {
        return flowinstrs;
    }

    public void addFlowinstr(Flowinstr flowinstr) {
        this.flowinstrs.add(flowinstr);
    }
    public List<FlowInstr> getFlowinstrs() {
        return flowinstrs;
    }

    public void addFlowinstr(Flowinstr flowinstr) {
        this.flowinstrs.add(flowinstr);
    }

}
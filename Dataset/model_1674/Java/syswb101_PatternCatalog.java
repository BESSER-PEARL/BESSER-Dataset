





import java.util.List;
import java.util.ArrayList;

public class syswb101_PatternCatalog  {

    private String id;





    private syswb101_Workbench syswb101_workbench;




    private List<syswb101_Function> syswb101_functions;


    public syswb101_PatternCatalog(
        String id    ) {
        this.id = id;
        this.syswb101_functions = new ArrayList<>();
    }

    public syswb101_PatternCatalog(
        String id        ArrayList<syswb101_Function> syswb101_functions    ) {
        this.id = id;
        this.syswb101_functions = syswb101_functions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public syswb101_Workbench getSyswb101_workbench() {
        return syswb101_workbench;
    }

    public void setSyswb101_workbench(syswb101_Workbench syswb101_workbench) {
        this.syswb101_workbench = syswb101_workbench;
    }
    public List<syswb101_Function> getSyswb101_functions() {
        return syswb101_functions;
    }

    public void addSyswb101_function(Syswb101_function syswb101_function) {
        this.syswb101_functions.add(syswb101_function);
    }

}
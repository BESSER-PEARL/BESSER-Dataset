





import java.util.List;
import java.util.ArrayList;

public class syswbeff106_PatternCatalog  {

    private String id;





    private List<syswbeff106_Function> syswbeff106_functions;


    public syswbeff106_PatternCatalog(
        String id    ) {
        this.id = id;
        this.syswbeff106_functions = new ArrayList<>();
    }

    public syswbeff106_PatternCatalog(
        String id        ArrayList<syswbeff106_Function> syswbeff106_functions    ) {
        this.id = id;
        this.syswbeff106_functions = syswbeff106_functions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<syswbeff106_Function> getSyswbeff106_functions() {
        return syswbeff106_functions;
    }

    public void addSyswbeff106_function(Syswbeff106_function syswbeff106_function) {
        this.syswbeff106_functions.add(syswbeff106_function);
    }

}
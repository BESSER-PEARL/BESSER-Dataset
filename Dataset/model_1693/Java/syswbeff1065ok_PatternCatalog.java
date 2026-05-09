





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_PatternCatalog  {

    private String id;





    private List<syswbeff1065ok_Function> syswbeff1065ok_functions;


    public syswbeff1065ok_PatternCatalog(
        String id    ) {
        this.id = id;
        this.syswbeff1065ok_functions = new ArrayList<>();
    }

    public syswbeff1065ok_PatternCatalog(
        String id        ArrayList<syswbeff1065ok_Function> syswbeff1065ok_functions    ) {
        this.id = id;
        this.syswbeff1065ok_functions = syswbeff1065ok_functions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<syswbeff1065ok_Function> getSyswbeff1065ok_functions() {
        return syswbeff1065ok_functions;
    }

    public void addSyswbeff1065ok_function(Syswbeff1065ok_function syswbeff1065ok_function) {
        this.syswbeff1065ok_functions.add(syswbeff1065ok_function);
    }

}
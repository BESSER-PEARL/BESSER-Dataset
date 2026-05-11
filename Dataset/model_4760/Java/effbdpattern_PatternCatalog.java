





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_PatternCatalog  {

    private String id;





    private List<effbdpattern_SystemPattern> effbdpattern_systempatterns;




    private List<effbdpattern_Function> effbdpattern_functions;


    public effbdpattern_PatternCatalog(
        String id    ) {
        this.id = id;
        this.effbdpattern_systempatterns = new ArrayList<>();
        this.effbdpattern_functions = new ArrayList<>();
    }

    public effbdpattern_PatternCatalog(
        String id        ArrayList<effbdpattern_SystemPattern> effbdpattern_systempatterns,        ArrayList<effbdpattern_Function> effbdpattern_functions    ) {
        this.id = id;
        this.effbdpattern_systempatterns = effbdpattern_systempatterns;
        this.effbdpattern_functions = effbdpattern_functions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<effbdpattern_SystemPattern> getEffbdpattern_systempatterns() {
        return effbdpattern_systempatterns;
    }

    public void addEffbdpattern_systempattern(Effbdpattern_systempattern effbdpattern_systempattern) {
        this.effbdpattern_systempatterns.add(effbdpattern_systempattern);
    }
    public List<effbdpattern_Function> getEffbdpattern_functions() {
        return effbdpattern_functions;
    }

    public void addEffbdpattern_function(Effbdpattern_function effbdpattern_function) {
        this.effbdpattern_functions.add(effbdpattern_function);
    }

}
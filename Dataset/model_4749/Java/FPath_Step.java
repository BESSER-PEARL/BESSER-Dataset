





import java.util.List;
import java.util.ArrayList;

public class FPath_Step extends LocatedElement {

    private String axis;





    private FPath_Test fpath_test;




    private List<FPath_Expression> fpath_expressions;


    public FPath_Step(
        String axis    ) {
        super(
        );
        this.axis = axis;
        this.fpath_expressions = new ArrayList<>();
    }

    public FPath_Step(
        String axis        ArrayList<FPath_Expression> fpath_expressions    ) {
        this.axis = axis;
        this.fpath_expressions = fpath_expressions;
    }

    public String getAxis() {
        return axis;
    }

    public void setAxis(String axis) {
        this.axis = axis;
    }

    public FPath_Test getFpath_test() {
        return fpath_test;
    }

    public void setFpath_test(FPath_Test fpath_test) {
        this.fpath_test = fpath_test;
    }
    public List<FPath_Expression> getFpath_expressions() {
        return fpath_expressions;
    }

    public void addFpath_expression(Fpath_expression fpath_expression) {
        this.fpath_expressions.add(fpath_expression);
    }

}
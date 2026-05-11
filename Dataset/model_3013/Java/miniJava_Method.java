





import java.util.List;
import java.util.ArrayList;

public class miniJava_Method extends Member {

    private boolean isabstract;
    private boolean isstatic;





    private List<miniJava_Parameter> minijava_parameters;


    public miniJava_Method(
        boolean isabstract,        boolean isstatic    ) {
        super(
        );
        this.isabstract = isabstract;
        this.isstatic = isstatic;
        this.minijava_parameters = new ArrayList<>();
    }

    public miniJava_Method(
        boolean isabstract,        boolean isstatic        ArrayList<miniJava_Parameter> minijava_parameters    ) {
        this.isabstract = isabstract;
        this.isstatic = isstatic;
        this.minijava_parameters = minijava_parameters;
    }

    public boolean getIsabstract() {
        return isabstract;
    }

    public void setIsabstract(boolean isabstract) {
        this.isabstract = isabstract;
    }
    public boolean getIsstatic() {
        return isstatic;
    }

    public void setIsstatic(boolean isstatic) {
        this.isstatic = isstatic;
    }

    public List<miniJava_Parameter> getMinijava_parameters() {
        return minijava_parameters;
    }

    public void addMinijava_parameter(Minijava_parameter minijava_parameter) {
        this.minijava_parameters.add(minijava_parameter);
    }

}
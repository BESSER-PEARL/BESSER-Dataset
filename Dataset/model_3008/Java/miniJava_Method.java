





import java.util.List;
import java.util.ArrayList;

public class miniJava_Method extends Member {

    private boolean isabstract;
    private boolean isstatic;





    private List<miniJava_Parameter> minijava_parameters;




    private miniJava_ClazzToMethodMap minijava_clazztomethodmap;




    private List<miniJava_ClazzToMethodMap> minijava_clazztomethodmaps;




    private miniJava_Block minijava_block;


    public miniJava_Method(
        boolean isabstract,        boolean isstatic    ) {
        super(
        );
        this.isabstract = isabstract;
        this.isstatic = isstatic;
        this.minijava_parameters = new ArrayList<>();
        this.minijava_clazztomethodmaps = new ArrayList<>();
    }

    public miniJava_Method(
        boolean isabstract,        boolean isstatic        ArrayList<miniJava_Parameter> minijava_parameters,        ArrayList<miniJava_ClazzToMethodMap> minijava_clazztomethodmaps    ) {
        this.isabstract = isabstract;
        this.isstatic = isstatic;
        this.minijava_parameters = minijava_parameters;
        this.minijava_clazztomethodmaps = minijava_clazztomethodmaps;
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
    public miniJava_ClazzToMethodMap getMinijava_clazztomethodmap() {
        return minijava_clazztomethodmap;
    }

    public void setMinijava_clazztomethodmap(miniJava_ClazzToMethodMap minijava_clazztomethodmap) {
        this.minijava_clazztomethodmap = minijava_clazztomethodmap;
    }
    public List<miniJava_ClazzToMethodMap> getMinijava_clazztomethodmaps() {
        return minijava_clazztomethodmaps;
    }

    public void addMinijava_clazztomethodmap(Minijava_clazztomethodmap minijava_clazztomethodmap) {
        this.minijava_clazztomethodmaps.add(minijava_clazztomethodmap);
    }
    public miniJava_Block getMinijava_block() {
        return minijava_block;
    }

    public void setMinijava_block(miniJava_Block minijava_block) {
        this.minijava_block = minijava_block;
    }

}
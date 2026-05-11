





import java.util.List;
import java.util.ArrayList;

public class miniJava_Method extends Member {

    private boolean isstatic;
    private boolean isabstract;





    private List<miniJava_ClazzToMethodMap> minijava_clazztomethodmaps;




    private List<miniJava_Parameter> minijava_parameters;




    private miniJava_ClazzToMethodMap minijava_clazztomethodmap;




    private miniJava_Block minijava_block;


    public miniJava_Method(
        boolean isstatic,        boolean isabstract    ) {
        super(
        );
        this.isstatic = isstatic;
        this.isabstract = isabstract;
        this.minijava_clazztomethodmaps = new ArrayList<>();
        this.minijava_parameters = new ArrayList<>();
    }

    public miniJava_Method(
        boolean isstatic,        boolean isabstract        ArrayList<miniJava_ClazzToMethodMap> minijava_clazztomethodmaps,        ArrayList<miniJava_Parameter> minijava_parameters    ) {
        this.isstatic = isstatic;
        this.isabstract = isabstract;
        this.minijava_clazztomethodmaps = minijava_clazztomethodmaps;
        this.minijava_parameters = minijava_parameters;
    }

    public boolean getIsstatic() {
        return isstatic;
    }

    public void setIsstatic(boolean isstatic) {
        this.isstatic = isstatic;
    }
    public boolean getIsabstract() {
        return isabstract;
    }

    public void setIsabstract(boolean isabstract) {
        this.isabstract = isabstract;
    }

    public List<miniJava_ClazzToMethodMap> getMinijava_clazztomethodmaps() {
        return minijava_clazztomethodmaps;
    }

    public void addMinijava_clazztomethodmap(Minijava_clazztomethodmap minijava_clazztomethodmap) {
        this.minijava_clazztomethodmaps.add(minijava_clazztomethodmap);
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
    public miniJava_Block getMinijava_block() {
        return minijava_block;
    }

    public void setMinijava_block(miniJava_Block minijava_block) {
        this.minijava_block = minijava_block;
    }

}
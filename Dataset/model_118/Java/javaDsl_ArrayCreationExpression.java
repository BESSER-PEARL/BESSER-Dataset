





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ArrayCreationExpression  {

    private String type;
    private String layers;





    private List<javaDsl_ArrayExpression> javadsl_arrayexpressions;




    private javaDsl_PrimaryNewArray javadsl_primarynewarray;


    public javaDsl_ArrayCreationExpression(
        String type,        String layers    ) {
        this.type = type;
        this.layers = layers;
        this.javadsl_arrayexpressions = new ArrayList<>();
    }

    public javaDsl_ArrayCreationExpression(
        String type,        String layers        ArrayList<javaDsl_ArrayExpression> javadsl_arrayexpressions    ) {
        this.type = type;
        this.layers = layers;
        this.javadsl_arrayexpressions = javadsl_arrayexpressions;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getLayers() {
        return layers;
    }

    public void setLayers(String layers) {
        this.layers = layers;
    }

    public List<javaDsl_ArrayExpression> getJavadsl_arrayexpressions() {
        return javadsl_arrayexpressions;
    }

    public void addJavadsl_arrayexpression(Javadsl_arrayexpression javadsl_arrayexpression) {
        this.javadsl_arrayexpressions.add(javadsl_arrayexpression);
    }
    public javaDsl_PrimaryNewArray getJavadsl_primarynewarray() {
        return javadsl_primarynewarray;
    }

    public void setJavadsl_primarynewarray(javaDsl_PrimaryNewArray javadsl_primarynewarray) {
        this.javadsl_primarynewarray = javadsl_primarynewarray;
    }

}
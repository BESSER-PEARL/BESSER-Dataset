





import java.util.List;
import java.util.ArrayList;

public class vql_Annotation  {

    private String name;





    private vql_Pattern vql_pattern;




    private List<vql_AnnotationParameter> vql_annotationparameters;


    public vql_Annotation(
        String name    ) {
        this.name = name;
        this.vql_annotationparameters = new ArrayList<>();
    }

    public vql_Annotation(
        String name        ArrayList<vql_AnnotationParameter> vql_annotationparameters    ) {
        this.name = name;
        this.vql_annotationparameters = vql_annotationparameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vql_Pattern getVql_pattern() {
        return vql_pattern;
    }

    public void setVql_pattern(vql_Pattern vql_pattern) {
        this.vql_pattern = vql_pattern;
    }
    public List<vql_AnnotationParameter> getVql_annotationparameters() {
        return vql_annotationparameters;
    }

    public void addVql_annotationparameter(Vql_annotationparameter vql_annotationparameter) {
        this.vql_annotationparameters.add(vql_annotationparameter);
    }

}
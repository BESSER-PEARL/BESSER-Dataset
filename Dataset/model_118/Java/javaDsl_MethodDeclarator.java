





import java.util.List;
import java.util.ArrayList;

public class javaDsl_MethodDeclarator  {

    private String name;





    private javaDsl_MethodHeader javadsl_methodheader;




    private List<javaDsl_FormalParameter> javadsl_formalparameters;


    public javaDsl_MethodDeclarator(
        String name    ) {
        this.name = name;
        this.javadsl_formalparameters = new ArrayList<>();
    }

    public javaDsl_MethodDeclarator(
        String name        ArrayList<javaDsl_FormalParameter> javadsl_formalparameters    ) {
        this.name = name;
        this.javadsl_formalparameters = javadsl_formalparameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public javaDsl_MethodHeader getJavadsl_methodheader() {
        return javadsl_methodheader;
    }

    public void setJavadsl_methodheader(javaDsl_MethodHeader javadsl_methodheader) {
        this.javadsl_methodheader = javadsl_methodheader;
    }
    public List<javaDsl_FormalParameter> getJavadsl_formalparameters() {
        return javadsl_formalparameters;
    }

    public void addJavadsl_formalparameter(Javadsl_formalparameter javadsl_formalparameter) {
        this.javadsl_formalparameters.add(javadsl_formalparameter);
    }

}






import java.util.List;
import java.util.ArrayList;

public class simplejava_Method  {

    private String name;
    private boolean static;





    private simplejava_ClassDeclaration simplejava_classdeclaration;




    private List<simplejava_Parameter> simplejava_parameters;


    public simplejava_Method(
        String name,        boolean static    ) {
        this.name = name;
        this.static = static;
        this.simplejava_parameters = new ArrayList<>();
    }

    public simplejava_Method(
        String name,        boolean static        ArrayList<simplejava_Parameter> simplejava_parameters    ) {
        this.name = name;
        this.static = static;
        this.simplejava_parameters = simplejava_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public simplejava_ClassDeclaration getSimplejava_classdeclaration() {
        return simplejava_classdeclaration;
    }

    public void setSimplejava_classdeclaration(simplejava_ClassDeclaration simplejava_classdeclaration) {
        this.simplejava_classdeclaration = simplejava_classdeclaration;
    }
    public List<simplejava_Parameter> getSimplejava_parameters() {
        return simplejava_parameters;
    }

    public void addSimplejava_parameter(Simplejava_parameter simplejava_parameter) {
        this.simplejava_parameters.add(simplejava_parameter);
    }

}
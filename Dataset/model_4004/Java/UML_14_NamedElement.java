





import java.util.List;
import java.util.ArrayList;

public class UML_14_NamedElement  {

    private String name;





    private List<UML_14_Comment> uml_14_comments;




    private List<UML_14_Constraint> uml_14_constraints;


    public UML_14_NamedElement(
        String name    ) {
        this.name = name;
        this.uml_14_comments = new ArrayList<>();
        this.uml_14_constraints = new ArrayList<>();
    }

    public UML_14_NamedElement(
        String name        ArrayList<UML_14_Comment> uml_14_comments,        ArrayList<UML_14_Constraint> uml_14_constraints    ) {
        this.name = name;
        this.uml_14_comments = uml_14_comments;
        this.uml_14_constraints = uml_14_constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UML_14_Comment> getUml_14_comments() {
        return uml_14_comments;
    }

    public void addUml_14_comment(Uml_14_comment uml_14_comment) {
        this.uml_14_comments.add(uml_14_comment);
    }
    public List<UML_14_Constraint> getUml_14_constraints() {
        return uml_14_constraints;
    }

    public void addUml_14_constraint(Uml_14_constraint uml_14_constraint) {
        this.uml_14_constraints.add(uml_14_constraint);
    }

}
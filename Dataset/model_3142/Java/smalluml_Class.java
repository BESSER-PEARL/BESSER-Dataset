





import java.util.List;
import java.util.ArrayList;

public class smalluml_Class extends NamedElement {

    private boolean isAbstract;





    private List<smalluml_Class> smalluml_classs;




    private List<smalluml_Method> smalluml_methods;




    private smalluml_Relation smalluml_relation;




    private smalluml_Relation smalluml_relation;


    public smalluml_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.smalluml_classs = new ArrayList<>();
        this.smalluml_methods = new ArrayList<>();
    }

    public smalluml_Class(
        boolean isAbstract        ArrayList<smalluml_Class> smalluml_classs,        ArrayList<smalluml_Method> smalluml_methods    ) {
        this.isAbstract = isAbstract;
        this.smalluml_classs = smalluml_classs;
        this.smalluml_methods = smalluml_methods;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<smalluml_Class> getSmalluml_classs() {
        return smalluml_classs;
    }

    public void addSmalluml_class(Smalluml_class smalluml_class) {
        this.smalluml_classs.add(smalluml_class);
    }
    public List<smalluml_Method> getSmalluml_methods() {
        return smalluml_methods;
    }

    public void addSmalluml_method(Smalluml_method smalluml_method) {
        this.smalluml_methods.add(smalluml_method);
    }
    public smalluml_Relation getSmalluml_relation() {
        return smalluml_relation;
    }

    public void setSmalluml_relation(smalluml_Relation smalluml_relation) {
        this.smalluml_relation = smalluml_relation;
    }
    public smalluml_Relation getSmalluml_relation() {
        return smalluml_relation;
    }

    public void setSmalluml_relation(smalluml_Relation smalluml_relation) {
        this.smalluml_relation = smalluml_relation;
    }

}
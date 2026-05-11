





import java.util.List;
import java.util.ArrayList;

public class smalluml_Role extends NamedElement {

    private int upperBound;
    private int lowerBound;





    private smalluml_Class smalluml_class;




    private smalluml_Relation smalluml_relation;




    private smalluml_Relation smalluml_relation;


    public smalluml_Role(
        int upperBound,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public smalluml_Class getSmalluml_class() {
        return smalluml_class;
    }

    public void setSmalluml_class(smalluml_Class smalluml_class) {
        this.smalluml_class = smalluml_class;
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
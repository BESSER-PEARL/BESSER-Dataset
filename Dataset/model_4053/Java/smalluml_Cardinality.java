





import java.util.List;
import java.util.ArrayList;

public class smalluml_Cardinality extends NamedElement {

    private int upperBound;
    private int lowerBound;





    private smalluml_Relation smalluml_relation;


    public smalluml_Cardinality(
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

    public smalluml_Relation getSmalluml_relation() {
        return smalluml_relation;
    }

    public void setSmalluml_relation(smalluml_Relation smalluml_relation) {
        this.smalluml_relation = smalluml_relation;
    }

}
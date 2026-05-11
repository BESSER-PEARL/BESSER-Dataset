





import java.util.List;
import java.util.ArrayList;

public class smalluml_Role  {

    private String Multiplicity;





    private smalluml_Association smalluml_association;




    private smalluml_SmallClass smalluml_smallclass;


    public smalluml_Role(
        String Multiplicity    ) {
        this.Multiplicity = Multiplicity;
    }


    public String getMultiplicity() {
        return Multiplicity;
    }

    public void setMultiplicity(String Multiplicity) {
        this.Multiplicity = Multiplicity;
    }

    public smalluml_Association getSmalluml_association() {
        return smalluml_association;
    }

    public void setSmalluml_association(smalluml_Association smalluml_association) {
        this.smalluml_association = smalluml_association;
    }
    public smalluml_SmallClass getSmalluml_smallclass() {
        return smalluml_smallclass;
    }

    public void setSmalluml_smallclass(smalluml_SmallClass smalluml_smallclass) {
        this.smalluml_smallclass = smalluml_smallclass;
    }

}
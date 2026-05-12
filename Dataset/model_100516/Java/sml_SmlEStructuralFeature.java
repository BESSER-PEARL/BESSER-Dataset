





import java.util.List;
import java.util.ArrayList;

public class sml_SmlEStructuralFeature  {

    private String name;





    private sml_StructuralFeatureValue sml_structuralfeaturevalue;


    public sml_SmlEStructuralFeature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_StructuralFeatureValue getSml_structuralfeaturevalue() {
        return sml_structuralfeaturevalue;
    }

    public void setSml_structuralfeaturevalue(sml_StructuralFeatureValue sml_structuralfeaturevalue) {
        this.sml_structuralfeaturevalue = sml_structuralfeaturevalue;
    }

}
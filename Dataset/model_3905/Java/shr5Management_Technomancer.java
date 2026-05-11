





import java.util.List;
import java.util.ArrayList;

public class shr5Management_Technomancer extends SpecialType {

    private int complexForms;
    private int resonanz;



    public shr5Management_Technomancer(
        int complexForms,        int resonanz    ) {
        super(
        );
        this.complexForms = complexForms;
        this.resonanz = resonanz;
    }


    public int getComplexforms() {
        return complexForms;
    }

    public void setComplexforms(int complexForms) {
        this.complexForms = complexForms;
    }
    public int getResonanz() {
        return resonanz;
    }

    public void setResonanz(int resonanz) {
        this.resonanz = resonanz;
    }


}
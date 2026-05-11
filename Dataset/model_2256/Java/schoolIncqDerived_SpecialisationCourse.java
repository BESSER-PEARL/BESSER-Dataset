





import java.util.List;
import java.util.ArrayList;

public class schoolIncqDerived_SpecialisationCourse extends Course {

    private String specialisation;



    public schoolIncqDerived_SpecialisationCourse(
        String specialisation    ) {
        super(
        );
        this.specialisation = specialisation;
    }


    public String getSpecialisation() {
        return specialisation;
    }

    public void setSpecialisation(String specialisation) {
        this.specialisation = specialisation;
    }


}
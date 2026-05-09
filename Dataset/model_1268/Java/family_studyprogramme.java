





import java.util.List;
import java.util.ArrayList;

public class family_studyprogramme  {

    private String name;





    private family_university family_university;


    public family_studyprogramme(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public family_university getFamily_university() {
        return family_university;
    }

    public void setFamily_university(family_university family_university) {
        this.family_university = family_university;
    }

}
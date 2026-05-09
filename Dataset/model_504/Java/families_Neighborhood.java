





import java.util.List;
import java.util.ArrayList;

public class families_Neighborhood extends NamedElement {






    private families_City families_city;




    private List<families_School> families_schools;


    public families_Neighborhood(
    ) {
        super(
        );
        this.families_schools = new ArrayList<>();
    }

    public families_Neighborhood(
        ArrayList<families_School> families_schools    ) {
        this.families_schools = families_schools;
    }


    public families_City getFamilies_city() {
        return families_city;
    }

    public void setFamilies_city(families_City families_city) {
        this.families_city = families_city;
    }
    public List<families_School> getFamilies_schools() {
        return families_schools;
    }

    public void addFamilies_school(Families_school families_school) {
        this.families_schools.add(families_school);
    }

}
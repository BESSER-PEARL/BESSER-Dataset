





import java.util.List;
import java.util.ArrayList;

public class families_Company extends NamedElement {






    private List<families_City> families_citys;




    private families_Country families_country;




    private families_City families_city;


    public families_Company(
    ) {
        super(
        );
        this.families_citys = new ArrayList<>();
    }

    public families_Company(
        ArrayList<families_City> families_citys    ) {
        this.families_citys = families_citys;
    }


    public List<families_City> getFamilies_citys() {
        return families_citys;
    }

    public void addFamilies_city(Families_city families_city) {
        this.families_citys.add(families_city);
    }
    public families_Country getFamilies_country() {
        return families_country;
    }

    public void setFamilies_country(families_Country families_country) {
        this.families_country = families_country;
    }
    public families_City getFamilies_city() {
        return families_city;
    }

    public void setFamilies_city(families_City families_city) {
        this.families_city = families_city;
    }

}
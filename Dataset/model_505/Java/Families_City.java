





import java.util.List;
import java.util.ArrayList;

public class Families_City extends NamedElement {






    private List<Families_Neighborhood> families_neighborhoods;




    private List<Families_Company> families_companys;




    private Families_Country families_country;




    private Families_Company families_company;


    public Families_City(
    ) {
        super(
        );
        this.families_neighborhoods = new ArrayList<>();
        this.families_companys = new ArrayList<>();
    }

    public Families_City(
        ArrayList<Families_Neighborhood> families_neighborhoods,        ArrayList<Families_Company> families_companys    ) {
        this.families_neighborhoods = families_neighborhoods;
        this.families_companys = families_companys;
    }


    public List<Families_Neighborhood> getFamilies_neighborhoods() {
        return families_neighborhoods;
    }

    public void addFamilies_neighborhood(Families_neighborhood families_neighborhood) {
        this.families_neighborhoods.add(families_neighborhood);
    }
    public List<Families_Company> getFamilies_companys() {
        return families_companys;
    }

    public void addFamilies_company(Families_company families_company) {
        this.families_companys.add(families_company);
    }
    public Families_Country getFamilies_country() {
        return families_country;
    }

    public void setFamilies_country(Families_Country families_country) {
        this.families_country = families_country;
    }
    public Families_Company getFamilies_company() {
        return families_company;
    }

    public void setFamilies_company(Families_Company families_company) {
        this.families_company = families_company;
    }

}
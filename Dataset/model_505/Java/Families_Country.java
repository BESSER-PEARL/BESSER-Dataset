





import java.util.List;
import java.util.ArrayList;

public class Families_Country extends NamedElement {






    private List<Families_Company> families_companys;


    public Families_Country(
    ) {
        super(
        );
        this.families_companys = new ArrayList<>();
    }

    public Families_Country(
        ArrayList<Families_Company> families_companys    ) {
        this.families_companys = families_companys;
    }


    public List<Families_Company> getFamilies_companys() {
        return families_companys;
    }

    public void addFamilies_company(Families_company families_company) {
        this.families_companys.add(families_company);
    }

}
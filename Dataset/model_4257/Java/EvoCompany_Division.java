





import java.util.List;
import java.util.ArrayList;

public class EvoCompany_Division  {

    private String name;





    private EvoCompany_Organisation evocompany_organisation;


    public EvoCompany_Division(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public EvoCompany_Organisation getEvocompany_organisation() {
        return evocompany_organisation;
    }

    public void setEvocompany_organisation(EvoCompany_Organisation evocompany_organisation) {
        this.evocompany_organisation = evocompany_organisation;
    }

}
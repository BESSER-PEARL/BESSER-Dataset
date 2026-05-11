





import java.util.List;
import java.util.ArrayList;

public class EvoCompany_CompanyModel  {






    private EvoCompany_Organisation evocompany_organisation;




    private List<EvoCompany_Topic> evocompany_topics;




    private List<EvoCompany_Category> evocompany_categorys;




    private List<EvoCompany_Division> evocompany_divisions;


    public EvoCompany_CompanyModel(
    ) {
        this.evocompany_topics = new ArrayList<>();
        this.evocompany_categorys = new ArrayList<>();
        this.evocompany_divisions = new ArrayList<>();
    }

    public EvoCompany_CompanyModel(
        ArrayList<EvoCompany_Topic> evocompany_topics,        ArrayList<EvoCompany_Category> evocompany_categorys,        ArrayList<EvoCompany_Division> evocompany_divisions    ) {
        this.evocompany_topics = evocompany_topics;
        this.evocompany_categorys = evocompany_categorys;
        this.evocompany_divisions = evocompany_divisions;
    }


    public EvoCompany_Organisation getEvocompany_organisation() {
        return evocompany_organisation;
    }

    public void setEvocompany_organisation(EvoCompany_Organisation evocompany_organisation) {
        this.evocompany_organisation = evocompany_organisation;
    }
    public List<EvoCompany_Topic> getEvocompany_topics() {
        return evocompany_topics;
    }

    public void addEvocompany_topic(Evocompany_topic evocompany_topic) {
        this.evocompany_topics.add(evocompany_topic);
    }
    public List<EvoCompany_Category> getEvocompany_categorys() {
        return evocompany_categorys;
    }

    public void addEvocompany_category(Evocompany_category evocompany_category) {
        this.evocompany_categorys.add(evocompany_category);
    }
    public List<EvoCompany_Division> getEvocompany_divisions() {
        return evocompany_divisions;
    }

    public void addEvocompany_division(Evocompany_division evocompany_division) {
        this.evocompany_divisions.add(evocompany_division);
    }

}
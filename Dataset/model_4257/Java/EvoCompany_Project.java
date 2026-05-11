





import java.util.List;
import java.util.ArrayList;

public class EvoCompany_Project  {

    private int budget;
    private String name;





    private EvoCompany_Person evocompany_person;




    private EvoCompany_Topic evocompany_topic;


    public EvoCompany_Project(
        int budget,        String name    ) {
        this.budget = budget;
        this.name = name;
    }


    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public EvoCompany_Person getEvocompany_person() {
        return evocompany_person;
    }

    public void setEvocompany_person(EvoCompany_Person evocompany_person) {
        this.evocompany_person = evocompany_person;
    }
    public EvoCompany_Topic getEvocompany_topic() {
        return evocompany_topic;
    }

    public void setEvocompany_topic(EvoCompany_Topic evocompany_topic) {
        this.evocompany_topic = evocompany_topic;
    }

}
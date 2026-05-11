





import java.util.List;
import java.util.ArrayList;

public class EvoCompany_Category  {

    private String name;





    private List<EvoCompany_Topic> evocompany_topics;




    private EvoCompany_Topic evocompany_topic;


    public EvoCompany_Category(
        String name    ) {
        this.name = name;
        this.evocompany_topics = new ArrayList<>();
    }

    public EvoCompany_Category(
        String name        ArrayList<EvoCompany_Topic> evocompany_topics    ) {
        this.name = name;
        this.evocompany_topics = evocompany_topics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<EvoCompany_Topic> getEvocompany_topics() {
        return evocompany_topics;
    }

    public void addEvocompany_topic(Evocompany_topic evocompany_topic) {
        this.evocompany_topics.add(evocompany_topic);
    }
    public EvoCompany_Topic getEvocompany_topic() {
        return evocompany_topic;
    }

    public void setEvocompany_topic(EvoCompany_Topic evocompany_topic) {
        this.evocompany_topic = evocompany_topic;
    }

}






import java.util.List;
import java.util.ArrayList;

public class rankPL_AbstractDefinition  {

    private String name;





    private rankPL_Model rankpl_model;


    public rankPL_AbstractDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rankPL_Model getRankpl_model() {
        return rankpl_model;
    }

    public void setRankpl_model(rankPL_Model rankpl_model) {
        this.rankpl_model = rankpl_model;
    }

}
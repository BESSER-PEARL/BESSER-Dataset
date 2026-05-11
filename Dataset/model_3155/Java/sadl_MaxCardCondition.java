





import java.util.List;
import java.util.ArrayList;

public class sadl_MaxCardCondition extends Condition {

    private String card;





    private sadl_ResourceIdentifier sadl_resourceidentifier;




    private sadl_MaxCardinality sadl_maxcardinality;


    public sadl_MaxCardCondition(
        String card    ) {
        super(
        );
        this.card = card;
    }


    public String getCard() {
        return card;
    }

    public void setCard(String card) {
        this.card = card;
    }

    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }
    public sadl_MaxCardinality getSadl_maxcardinality() {
        return sadl_maxcardinality;
    }

    public void setSadl_maxcardinality(sadl_MaxCardinality sadl_maxcardinality) {
        this.sadl_maxcardinality = sadl_maxcardinality;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sadl_MinCardCondition extends Condition {

    private String card;





    private sadl_ResourceIdentifier sadl_resourceidentifier;




    private sadl_MinCardinality sadl_mincardinality;


    public sadl_MinCardCondition(
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
    public sadl_MinCardinality getSadl_mincardinality() {
        return sadl_mincardinality;
    }

    public void setSadl_mincardinality(sadl_MinCardinality sadl_mincardinality) {
        this.sadl_mincardinality = sadl_mincardinality;
    }

}
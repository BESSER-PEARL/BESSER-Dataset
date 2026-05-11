





import java.util.List;
import java.util.ArrayList;

public class sadl_CardCondition extends Condition {

    private String card;





    private sadl_ResourceIdentifier sadl_resourceidentifier;




    private sadl_Cardinality sadl_cardinality;


    public sadl_CardCondition(
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
    public sadl_Cardinality getSadl_cardinality() {
        return sadl_cardinality;
    }

    public void setSadl_cardinality(sadl_Cardinality sadl_cardinality) {
        this.sadl_cardinality = sadl_cardinality;
    }

}
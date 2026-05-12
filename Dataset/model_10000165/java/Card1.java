





import java.util.List;
import java.util.ArrayList;

public class Card1  {

    private None Rank;
    private String total_card;
    private int cardsRemianing;
    private None suit;



    public Card1(
        None Rank,        String total_card,        int cardsRemianing,        None suit    ) {
        this.Rank = Rank;
        this.total_card = total_card;
        this.cardsRemianing = cardsRemianing;
        this.suit = suit;
    }


    public None getRank() {
        return Rank;
    }

    public void setRank(None Rank) {
        this.Rank = Rank;
    }
    public String getTotal_card() {
        return total_card;
    }

    public void setTotal_card(String total_card) {
        this.total_card = total_card;
    }
    public int getCardsremianing() {
        return cardsRemianing;
    }

    public void setCardsremianing(int cardsRemianing) {
        this.cardsRemianing = cardsRemianing;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }


}
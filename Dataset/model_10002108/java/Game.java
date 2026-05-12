





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private None partnerCard;
    private None blind;
    private None picker;
    private None partner;
    private None deck;
    private None rounds_6_;
    private boolean isCracked;



    public Game(
        None partnerCard,        None blind,        None picker,        None partner,        None deck,        None rounds_6_,        boolean isCracked    ) {
        this.partnerCard = partnerCard;
        this.blind = blind;
        this.picker = picker;
        this.partner = partner;
        this.deck = deck;
        this.rounds_6_ = rounds_6_;
        this.isCracked = isCracked;
    }


    public None getPartnercard() {
        return partnerCard;
    }

    public void setPartnercard(None partnerCard) {
        this.partnerCard = partnerCard;
    }
    public None getBlind() {
        return blind;
    }

    public void setBlind(None blind) {
        this.blind = blind;
    }
    public None getPicker() {
        return picker;
    }

    public void setPicker(None picker) {
        this.picker = picker;
    }
    public None getPartner() {
        return partner;
    }

    public void setPartner(None partner) {
        this.partner = partner;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public None getRounds_6_() {
        return rounds_6_;
    }

    public void setRounds_6_(None rounds_6_) {
        this.rounds_6_ = rounds_6_;
    }
    public boolean getIscracked() {
        return isCracked;
    }

    public void setIscracked(boolean isCracked) {
        this.isCracked = isCracked;
    }


}
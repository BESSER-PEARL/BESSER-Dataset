





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String ACE;
    private String JACK;
    private String THREE;
    private String location;
    private String cardImageString;
    private boolean highlighted;
    private String cardBack;
    private String TWO;
    private String TEN;
    private String INVALID_NUMBER;
    private String cardNumber;
    private String HEARTS_SUIT;
    private String SIX;
    private String NINE;
    private String cardSuit;
    private String cardColor;
    private String INVALID_SUIT;
    private String int_deckNumber;
    private String FIVE;
    private String QUEEN;
    private String FOUR;
    private String fullCardNumber;
    private String cardHighLighted;
    private String CLUBS_SUIT;
    private String image;
    private String KING;
    private String SPADES_SUIT;
    private String DIAMONDS_SUIT;
    private boolean faceUp;
    private String SEVEN;
    private String EIGHT;



    public Card(
        String ACE,        String JACK,        String THREE,        String location,        String cardImageString,        boolean highlighted,        String cardBack,        String TWO,        String TEN,        String INVALID_NUMBER,        String cardNumber,        String HEARTS_SUIT,        String SIX,        String NINE,        String cardSuit,        String cardColor,        String INVALID_SUIT,        String int_deckNumber,        String FIVE,        String QUEEN,        String FOUR,        String fullCardNumber,        String cardHighLighted,        String CLUBS_SUIT,        String image,        String KING,        String SPADES_SUIT,        String DIAMONDS_SUIT,        boolean faceUp,        String SEVEN,        String EIGHT    ) {
        this.ACE = ACE;
        this.JACK = JACK;
        this.THREE = THREE;
        this.location = location;
        this.cardImageString = cardImageString;
        this.highlighted = highlighted;
        this.cardBack = cardBack;
        this.TWO = TWO;
        this.TEN = TEN;
        this.INVALID_NUMBER = INVALID_NUMBER;
        this.cardNumber = cardNumber;
        this.HEARTS_SUIT = HEARTS_SUIT;
        this.SIX = SIX;
        this.NINE = NINE;
        this.cardSuit = cardSuit;
        this.cardColor = cardColor;
        this.INVALID_SUIT = INVALID_SUIT;
        this.int_deckNumber = int_deckNumber;
        this.FIVE = FIVE;
        this.QUEEN = QUEEN;
        this.FOUR = FOUR;
        this.fullCardNumber = fullCardNumber;
        this.cardHighLighted = cardHighLighted;
        this.CLUBS_SUIT = CLUBS_SUIT;
        this.image = image;
        this.KING = KING;
        this.SPADES_SUIT = SPADES_SUIT;
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
        this.faceUp = faceUp;
        this.SEVEN = SEVEN;
        this.EIGHT = EIGHT;
    }


    public String getAce() {
        return ACE;
    }

    public void setAce(String ACE) {
        this.ACE = ACE;
    }
    public String getJack() {
        return JACK;
    }

    public void setJack(String JACK) {
        this.JACK = JACK;
    }
    public String getThree() {
        return THREE;
    }

    public void setThree(String THREE) {
        this.THREE = THREE;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getCardimagestring() {
        return cardImageString;
    }

    public void setCardimagestring(String cardImageString) {
        this.cardImageString = cardImageString;
    }
    public boolean getHighlighted() {
        return highlighted;
    }

    public void setHighlighted(boolean highlighted) {
        this.highlighted = highlighted;
    }
    public String getCardback() {
        return cardBack;
    }

    public void setCardback(String cardBack) {
        this.cardBack = cardBack;
    }
    public String getTwo() {
        return TWO;
    }

    public void setTwo(String TWO) {
        this.TWO = TWO;
    }
    public String getTen() {
        return TEN;
    }

    public void setTen(String TEN) {
        this.TEN = TEN;
    }
    public String getInvalid_number() {
        return INVALID_NUMBER;
    }

    public void setInvalid_number(String INVALID_NUMBER) {
        this.INVALID_NUMBER = INVALID_NUMBER;
    }
    public String getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }
    public String getHearts_suit() {
        return HEARTS_SUIT;
    }

    public void setHearts_suit(String HEARTS_SUIT) {
        this.HEARTS_SUIT = HEARTS_SUIT;
    }
    public String getSix() {
        return SIX;
    }

    public void setSix(String SIX) {
        this.SIX = SIX;
    }
    public String getNine() {
        return NINE;
    }

    public void setNine(String NINE) {
        this.NINE = NINE;
    }
    public String getCardsuit() {
        return cardSuit;
    }

    public void setCardsuit(String cardSuit) {
        this.cardSuit = cardSuit;
    }
    public String getCardcolor() {
        return cardColor;
    }

    public void setCardcolor(String cardColor) {
        this.cardColor = cardColor;
    }
    public String getInvalid_suit() {
        return INVALID_SUIT;
    }

    public void setInvalid_suit(String INVALID_SUIT) {
        this.INVALID_SUIT = INVALID_SUIT;
    }
    public String getInt_decknumber() {
        return int_deckNumber;
    }

    public void setInt_decknumber(String int_deckNumber) {
        this.int_deckNumber = int_deckNumber;
    }
    public String getFive() {
        return FIVE;
    }

    public void setFive(String FIVE) {
        this.FIVE = FIVE;
    }
    public String getQueen() {
        return QUEEN;
    }

    public void setQueen(String QUEEN) {
        this.QUEEN = QUEEN;
    }
    public String getFour() {
        return FOUR;
    }

    public void setFour(String FOUR) {
        this.FOUR = FOUR;
    }
    public String getFullcardnumber() {
        return fullCardNumber;
    }

    public void setFullcardnumber(String fullCardNumber) {
        this.fullCardNumber = fullCardNumber;
    }
    public String getCardhighlighted() {
        return cardHighLighted;
    }

    public void setCardhighlighted(String cardHighLighted) {
        this.cardHighLighted = cardHighLighted;
    }
    public String getClubs_suit() {
        return CLUBS_SUIT;
    }

    public void setClubs_suit(String CLUBS_SUIT) {
        this.CLUBS_SUIT = CLUBS_SUIT;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getKing() {
        return KING;
    }

    public void setKing(String KING) {
        this.KING = KING;
    }
    public String getSpades_suit() {
        return SPADES_SUIT;
    }

    public void setSpades_suit(String SPADES_SUIT) {
        this.SPADES_SUIT = SPADES_SUIT;
    }
    public String getDiamonds_suit() {
        return DIAMONDS_SUIT;
    }

    public void setDiamonds_suit(String DIAMONDS_SUIT) {
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
    }
    public boolean getFaceup() {
        return faceUp;
    }

    public void setFaceup(boolean faceUp) {
        this.faceUp = faceUp;
    }
    public String getSeven() {
        return SEVEN;
    }

    public void setSeven(String SEVEN) {
        this.SEVEN = SEVEN;
    }
    public String getEight() {
        return EIGHT;
    }

    public void setEight(String EIGHT) {
        this.EIGHT = EIGHT;
    }


}






import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String NINE;
    private String location;
    private String THREE;
    private boolean faceUp;
    private String image;
    private String EIGHT;
    private String JACK;
    private String CLUBS_SUIT;
    private boolean highlighted;
    private String fullCardNumber;
    private String KING;
    private String FIVE;
    private String DIAMONDS_SUIT;
    private String QUEEN;
    private String cardHighLighted;
    private String ACE;
    private String TWO;
    private String cardSuit;
    private String INVALID_NUMBER;
    private String HEARTS_SUIT;
    private String SIX;
    private String TEN;
    private String int_deckNumber;
    private String cardColor;
    private String SPADES_SUIT;
    private String INVALID_SUIT;
    private String SEVEN;
    private String cardNumber;
    private String cardImageString;
    private String cardBack;
    private String FOUR;



    public Card(
        String NINE,        String location,        String THREE,        boolean faceUp,        String image,        String EIGHT,        String JACK,        String CLUBS_SUIT,        boolean highlighted,        String fullCardNumber,        String KING,        String FIVE,        String DIAMONDS_SUIT,        String QUEEN,        String cardHighLighted,        String ACE,        String TWO,        String cardSuit,        String INVALID_NUMBER,        String HEARTS_SUIT,        String SIX,        String TEN,        String int_deckNumber,        String cardColor,        String SPADES_SUIT,        String INVALID_SUIT,        String SEVEN,        String cardNumber,        String cardImageString,        String cardBack,        String FOUR    ) {
        this.NINE = NINE;
        this.location = location;
        this.THREE = THREE;
        this.faceUp = faceUp;
        this.image = image;
        this.EIGHT = EIGHT;
        this.JACK = JACK;
        this.CLUBS_SUIT = CLUBS_SUIT;
        this.highlighted = highlighted;
        this.fullCardNumber = fullCardNumber;
        this.KING = KING;
        this.FIVE = FIVE;
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
        this.QUEEN = QUEEN;
        this.cardHighLighted = cardHighLighted;
        this.ACE = ACE;
        this.TWO = TWO;
        this.cardSuit = cardSuit;
        this.INVALID_NUMBER = INVALID_NUMBER;
        this.HEARTS_SUIT = HEARTS_SUIT;
        this.SIX = SIX;
        this.TEN = TEN;
        this.int_deckNumber = int_deckNumber;
        this.cardColor = cardColor;
        this.SPADES_SUIT = SPADES_SUIT;
        this.INVALID_SUIT = INVALID_SUIT;
        this.SEVEN = SEVEN;
        this.cardNumber = cardNumber;
        this.cardImageString = cardImageString;
        this.cardBack = cardBack;
        this.FOUR = FOUR;
    }


    public String getNine() {
        return NINE;
    }

    public void setNine(String NINE) {
        this.NINE = NINE;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getThree() {
        return THREE;
    }

    public void setThree(String THREE) {
        this.THREE = THREE;
    }
    public boolean getFaceup() {
        return faceUp;
    }

    public void setFaceup(boolean faceUp) {
        this.faceUp = faceUp;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getEight() {
        return EIGHT;
    }

    public void setEight(String EIGHT) {
        this.EIGHT = EIGHT;
    }
    public String getJack() {
        return JACK;
    }

    public void setJack(String JACK) {
        this.JACK = JACK;
    }
    public String getClubs_suit() {
        return CLUBS_SUIT;
    }

    public void setClubs_suit(String CLUBS_SUIT) {
        this.CLUBS_SUIT = CLUBS_SUIT;
    }
    public boolean getHighlighted() {
        return highlighted;
    }

    public void setHighlighted(boolean highlighted) {
        this.highlighted = highlighted;
    }
    public String getFullcardnumber() {
        return fullCardNumber;
    }

    public void setFullcardnumber(String fullCardNumber) {
        this.fullCardNumber = fullCardNumber;
    }
    public String getKing() {
        return KING;
    }

    public void setKing(String KING) {
        this.KING = KING;
    }
    public String getFive() {
        return FIVE;
    }

    public void setFive(String FIVE) {
        this.FIVE = FIVE;
    }
    public String getDiamonds_suit() {
        return DIAMONDS_SUIT;
    }

    public void setDiamonds_suit(String DIAMONDS_SUIT) {
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
    }
    public String getQueen() {
        return QUEEN;
    }

    public void setQueen(String QUEEN) {
        this.QUEEN = QUEEN;
    }
    public String getCardhighlighted() {
        return cardHighLighted;
    }

    public void setCardhighlighted(String cardHighLighted) {
        this.cardHighLighted = cardHighLighted;
    }
    public String getAce() {
        return ACE;
    }

    public void setAce(String ACE) {
        this.ACE = ACE;
    }
    public String getTwo() {
        return TWO;
    }

    public void setTwo(String TWO) {
        this.TWO = TWO;
    }
    public String getCardsuit() {
        return cardSuit;
    }

    public void setCardsuit(String cardSuit) {
        this.cardSuit = cardSuit;
    }
    public String getInvalid_number() {
        return INVALID_NUMBER;
    }

    public void setInvalid_number(String INVALID_NUMBER) {
        this.INVALID_NUMBER = INVALID_NUMBER;
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
    public String getTen() {
        return TEN;
    }

    public void setTen(String TEN) {
        this.TEN = TEN;
    }
    public String getInt_decknumber() {
        return int_deckNumber;
    }

    public void setInt_decknumber(String int_deckNumber) {
        this.int_deckNumber = int_deckNumber;
    }
    public String getCardcolor() {
        return cardColor;
    }

    public void setCardcolor(String cardColor) {
        this.cardColor = cardColor;
    }
    public String getSpades_suit() {
        return SPADES_SUIT;
    }

    public void setSpades_suit(String SPADES_SUIT) {
        this.SPADES_SUIT = SPADES_SUIT;
    }
    public String getInvalid_suit() {
        return INVALID_SUIT;
    }

    public void setInvalid_suit(String INVALID_SUIT) {
        this.INVALID_SUIT = INVALID_SUIT;
    }
    public String getSeven() {
        return SEVEN;
    }

    public void setSeven(String SEVEN) {
        this.SEVEN = SEVEN;
    }
    public String getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }
    public String getCardimagestring() {
        return cardImageString;
    }

    public void setCardimagestring(String cardImageString) {
        this.cardImageString = cardImageString;
    }
    public String getCardback() {
        return cardBack;
    }

    public void setCardback(String cardBack) {
        this.cardBack = cardBack;
    }
    public String getFour() {
        return FOUR;
    }

    public void setFour(String FOUR) {
        this.FOUR = FOUR;
    }


}
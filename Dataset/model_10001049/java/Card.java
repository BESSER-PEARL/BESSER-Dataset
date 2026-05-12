





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String cardHighlighted;
    private String cardImageString;
    private int JACK;
    private int EIGHT;
    private int ACE;
    private int TEN;
    private int cardColor;
    private String CLUBS_SUIT;
    private int INVALID_NUMBER;
    private int FOUR;
    private int THREE;
    private int fullCardNumber;
    private String INVALID_SUIT;
    private int cardNumber;
    private int SIX;
    private String cardBack;
    private String cardSuit;
    private int QUEEN;
    private int KING;
    private String DIAMONDS_SUIT;
    private int FIVE;
    private boolean faceUp;
    private int NINE;
    private String HEARTS_SUIT;
    private int SEVEN;
    private boolean highlighted;
    private String SPADES_SUIT;
    private String location;
    private int TWO;
    private String image;
    private int deckNumber;



    public Card(
        String cardHighlighted,        String cardImageString,        int JACK,        int EIGHT,        int ACE,        int TEN,        int cardColor,        String CLUBS_SUIT,        int INVALID_NUMBER,        int FOUR,        int THREE,        int fullCardNumber,        String INVALID_SUIT,        int cardNumber,        int SIX,        String cardBack,        String cardSuit,        int QUEEN,        int KING,        String DIAMONDS_SUIT,        int FIVE,        boolean faceUp,        int NINE,        String HEARTS_SUIT,        int SEVEN,        boolean highlighted,        String SPADES_SUIT,        String location,        int TWO,        String image,        int deckNumber    ) {
        this.cardHighlighted = cardHighlighted;
        this.cardImageString = cardImageString;
        this.JACK = JACK;
        this.EIGHT = EIGHT;
        this.ACE = ACE;
        this.TEN = TEN;
        this.cardColor = cardColor;
        this.CLUBS_SUIT = CLUBS_SUIT;
        this.INVALID_NUMBER = INVALID_NUMBER;
        this.FOUR = FOUR;
        this.THREE = THREE;
        this.fullCardNumber = fullCardNumber;
        this.INVALID_SUIT = INVALID_SUIT;
        this.cardNumber = cardNumber;
        this.SIX = SIX;
        this.cardBack = cardBack;
        this.cardSuit = cardSuit;
        this.QUEEN = QUEEN;
        this.KING = KING;
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
        this.FIVE = FIVE;
        this.faceUp = faceUp;
        this.NINE = NINE;
        this.HEARTS_SUIT = HEARTS_SUIT;
        this.SEVEN = SEVEN;
        this.highlighted = highlighted;
        this.SPADES_SUIT = SPADES_SUIT;
        this.location = location;
        this.TWO = TWO;
        this.image = image;
        this.deckNumber = deckNumber;
    }


    public String getCardhighlighted() {
        return cardHighlighted;
    }

    public void setCardhighlighted(String cardHighlighted) {
        this.cardHighlighted = cardHighlighted;
    }
    public String getCardimagestring() {
        return cardImageString;
    }

    public void setCardimagestring(String cardImageString) {
        this.cardImageString = cardImageString;
    }
    public int getJack() {
        return JACK;
    }

    public void setJack(int JACK) {
        this.JACK = JACK;
    }
    public int getEight() {
        return EIGHT;
    }

    public void setEight(int EIGHT) {
        this.EIGHT = EIGHT;
    }
    public int getAce() {
        return ACE;
    }

    public void setAce(int ACE) {
        this.ACE = ACE;
    }
    public int getTen() {
        return TEN;
    }

    public void setTen(int TEN) {
        this.TEN = TEN;
    }
    public int getCardcolor() {
        return cardColor;
    }

    public void setCardcolor(int cardColor) {
        this.cardColor = cardColor;
    }
    public String getClubs_suit() {
        return CLUBS_SUIT;
    }

    public void setClubs_suit(String CLUBS_SUIT) {
        this.CLUBS_SUIT = CLUBS_SUIT;
    }
    public int getInvalid_number() {
        return INVALID_NUMBER;
    }

    public void setInvalid_number(int INVALID_NUMBER) {
        this.INVALID_NUMBER = INVALID_NUMBER;
    }
    public int getFour() {
        return FOUR;
    }

    public void setFour(int FOUR) {
        this.FOUR = FOUR;
    }
    public int getThree() {
        return THREE;
    }

    public void setThree(int THREE) {
        this.THREE = THREE;
    }
    public int getFullcardnumber() {
        return fullCardNumber;
    }

    public void setFullcardnumber(int fullCardNumber) {
        this.fullCardNumber = fullCardNumber;
    }
    public String getInvalid_suit() {
        return INVALID_SUIT;
    }

    public void setInvalid_suit(String INVALID_SUIT) {
        this.INVALID_SUIT = INVALID_SUIT;
    }
    public int getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(int cardNumber) {
        this.cardNumber = cardNumber;
    }
    public int getSix() {
        return SIX;
    }

    public void setSix(int SIX) {
        this.SIX = SIX;
    }
    public String getCardback() {
        return cardBack;
    }

    public void setCardback(String cardBack) {
        this.cardBack = cardBack;
    }
    public String getCardsuit() {
        return cardSuit;
    }

    public void setCardsuit(String cardSuit) {
        this.cardSuit = cardSuit;
    }
    public int getQueen() {
        return QUEEN;
    }

    public void setQueen(int QUEEN) {
        this.QUEEN = QUEEN;
    }
    public int getKing() {
        return KING;
    }

    public void setKing(int KING) {
        this.KING = KING;
    }
    public String getDiamonds_suit() {
        return DIAMONDS_SUIT;
    }

    public void setDiamonds_suit(String DIAMONDS_SUIT) {
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
    }
    public int getFive() {
        return FIVE;
    }

    public void setFive(int FIVE) {
        this.FIVE = FIVE;
    }
    public boolean getFaceup() {
        return faceUp;
    }

    public void setFaceup(boolean faceUp) {
        this.faceUp = faceUp;
    }
    public int getNine() {
        return NINE;
    }

    public void setNine(int NINE) {
        this.NINE = NINE;
    }
    public String getHearts_suit() {
        return HEARTS_SUIT;
    }

    public void setHearts_suit(String HEARTS_SUIT) {
        this.HEARTS_SUIT = HEARTS_SUIT;
    }
    public int getSeven() {
        return SEVEN;
    }

    public void setSeven(int SEVEN) {
        this.SEVEN = SEVEN;
    }
    public boolean getHighlighted() {
        return highlighted;
    }

    public void setHighlighted(boolean highlighted) {
        this.highlighted = highlighted;
    }
    public String getSpades_suit() {
        return SPADES_SUIT;
    }

    public void setSpades_suit(String SPADES_SUIT) {
        this.SPADES_SUIT = SPADES_SUIT;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getTwo() {
        return TWO;
    }

    public void setTwo(int TWO) {
        this.TWO = TWO;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public int getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(int deckNumber) {
        this.deckNumber = deckNumber;
    }


}
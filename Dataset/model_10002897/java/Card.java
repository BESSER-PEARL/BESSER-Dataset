





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int TEN;
    private String cardSuit;
    private int SIX;
    private String location;
    private String INVALID_SUIT;
    private int JACK;
    private int FIVE;
    private int NINE;
    private int EIGHT;
    private int FOUR;
    private String cardImageString;
    private int ACE;
    private int INVALID_NUMBER;
    private int cardColor;
    private int deckNumber;
    private int THREE;
    private String cardBack;
    private boolean faceUp;
    private int TWO;
    private int KING;
    private int QUEEN;
    private boolean highlighted;
    private String DIAMONDS_SUIT;
    private String CLUBS_SUIT;
    private String SPADES_SUIT;
    private int cardNumber;
    private String HEARTS_SUIT;
    private String image;
    private int SEVEN;
    private int fullCardNumber;
    private String cardHighlighted;



    public Card(
        int TEN,        String cardSuit,        int SIX,        String location,        String INVALID_SUIT,        int JACK,        int FIVE,        int NINE,        int EIGHT,        int FOUR,        String cardImageString,        int ACE,        int INVALID_NUMBER,        int cardColor,        int deckNumber,        int THREE,        String cardBack,        boolean faceUp,        int TWO,        int KING,        int QUEEN,        boolean highlighted,        String DIAMONDS_SUIT,        String CLUBS_SUIT,        String SPADES_SUIT,        int cardNumber,        String HEARTS_SUIT,        String image,        int SEVEN,        int fullCardNumber,        String cardHighlighted    ) {
        this.TEN = TEN;
        this.cardSuit = cardSuit;
        this.SIX = SIX;
        this.location = location;
        this.INVALID_SUIT = INVALID_SUIT;
        this.JACK = JACK;
        this.FIVE = FIVE;
        this.NINE = NINE;
        this.EIGHT = EIGHT;
        this.FOUR = FOUR;
        this.cardImageString = cardImageString;
        this.ACE = ACE;
        this.INVALID_NUMBER = INVALID_NUMBER;
        this.cardColor = cardColor;
        this.deckNumber = deckNumber;
        this.THREE = THREE;
        this.cardBack = cardBack;
        this.faceUp = faceUp;
        this.TWO = TWO;
        this.KING = KING;
        this.QUEEN = QUEEN;
        this.highlighted = highlighted;
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
        this.CLUBS_SUIT = CLUBS_SUIT;
        this.SPADES_SUIT = SPADES_SUIT;
        this.cardNumber = cardNumber;
        this.HEARTS_SUIT = HEARTS_SUIT;
        this.image = image;
        this.SEVEN = SEVEN;
        this.fullCardNumber = fullCardNumber;
        this.cardHighlighted = cardHighlighted;
    }


    public int getTen() {
        return TEN;
    }

    public void setTen(int TEN) {
        this.TEN = TEN;
    }
    public String getCardsuit() {
        return cardSuit;
    }

    public void setCardsuit(String cardSuit) {
        this.cardSuit = cardSuit;
    }
    public int getSix() {
        return SIX;
    }

    public void setSix(int SIX) {
        this.SIX = SIX;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getInvalid_suit() {
        return INVALID_SUIT;
    }

    public void setInvalid_suit(String INVALID_SUIT) {
        this.INVALID_SUIT = INVALID_SUIT;
    }
    public int getJack() {
        return JACK;
    }

    public void setJack(int JACK) {
        this.JACK = JACK;
    }
    public int getFive() {
        return FIVE;
    }

    public void setFive(int FIVE) {
        this.FIVE = FIVE;
    }
    public int getNine() {
        return NINE;
    }

    public void setNine(int NINE) {
        this.NINE = NINE;
    }
    public int getEight() {
        return EIGHT;
    }

    public void setEight(int EIGHT) {
        this.EIGHT = EIGHT;
    }
    public int getFour() {
        return FOUR;
    }

    public void setFour(int FOUR) {
        this.FOUR = FOUR;
    }
    public String getCardimagestring() {
        return cardImageString;
    }

    public void setCardimagestring(String cardImageString) {
        this.cardImageString = cardImageString;
    }
    public int getAce() {
        return ACE;
    }

    public void setAce(int ACE) {
        this.ACE = ACE;
    }
    public int getInvalid_number() {
        return INVALID_NUMBER;
    }

    public void setInvalid_number(int INVALID_NUMBER) {
        this.INVALID_NUMBER = INVALID_NUMBER;
    }
    public int getCardcolor() {
        return cardColor;
    }

    public void setCardcolor(int cardColor) {
        this.cardColor = cardColor;
    }
    public int getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(int deckNumber) {
        this.deckNumber = deckNumber;
    }
    public int getThree() {
        return THREE;
    }

    public void setThree(int THREE) {
        this.THREE = THREE;
    }
    public String getCardback() {
        return cardBack;
    }

    public void setCardback(String cardBack) {
        this.cardBack = cardBack;
    }
    public boolean getFaceup() {
        return faceUp;
    }

    public void setFaceup(boolean faceUp) {
        this.faceUp = faceUp;
    }
    public int getTwo() {
        return TWO;
    }

    public void setTwo(int TWO) {
        this.TWO = TWO;
    }
    public int getKing() {
        return KING;
    }

    public void setKing(int KING) {
        this.KING = KING;
    }
    public int getQueen() {
        return QUEEN;
    }

    public void setQueen(int QUEEN) {
        this.QUEEN = QUEEN;
    }
    public boolean getHighlighted() {
        return highlighted;
    }

    public void setHighlighted(boolean highlighted) {
        this.highlighted = highlighted;
    }
    public String getDiamonds_suit() {
        return DIAMONDS_SUIT;
    }

    public void setDiamonds_suit(String DIAMONDS_SUIT) {
        this.DIAMONDS_SUIT = DIAMONDS_SUIT;
    }
    public String getClubs_suit() {
        return CLUBS_SUIT;
    }

    public void setClubs_suit(String CLUBS_SUIT) {
        this.CLUBS_SUIT = CLUBS_SUIT;
    }
    public String getSpades_suit() {
        return SPADES_SUIT;
    }

    public void setSpades_suit(String SPADES_SUIT) {
        this.SPADES_SUIT = SPADES_SUIT;
    }
    public int getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(int cardNumber) {
        this.cardNumber = cardNumber;
    }
    public String getHearts_suit() {
        return HEARTS_SUIT;
    }

    public void setHearts_suit(String HEARTS_SUIT) {
        this.HEARTS_SUIT = HEARTS_SUIT;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public int getSeven() {
        return SEVEN;
    }

    public void setSeven(int SEVEN) {
        this.SEVEN = SEVEN;
    }
    public int getFullcardnumber() {
        return fullCardNumber;
    }

    public void setFullcardnumber(int fullCardNumber) {
        this.fullCardNumber = fullCardNumber;
    }
    public String getCardhighlighted() {
        return cardHighlighted;
    }

    public void setCardhighlighted(String cardHighlighted) {
        this.cardHighlighted = cardHighlighted;
    }


}
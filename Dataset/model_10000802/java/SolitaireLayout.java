





import java.util.List;
import java.util.ArrayList;

public class SolitaireLayout  {

    private String deck;
    private String ColTwo;
    private String COLUMN_THREE;
    private String colOne;
    private String aceDiamonds;
    private String ColFour;
    private String cellFour;
    private String aceHearts;
    private String COLUMN_ONE;
    private String aceClubs;
    private String DIAMONDS_ACE_PILE;
    private String cellOne;
    private String discardPile;
    private String acespades;
    private String DECK;
    private String CELL_TWO;
    private String DISCARD_PILE;
    private String SPADES_ACE_PILE;
    private String ColThree;
    private String cellThree;
    private String HEARTS_ACE_PILE;
    private String CELL_ONE;
    private String COLUMN_FOUR;
    private String cellTwo;
    private String COLUMN_TWO;
    private String CELL_THREE;
    private String CLUBS_ACE_PILE;
    private String CELL_FOUR;



    public SolitaireLayout(
        String deck,        String ColTwo,        String COLUMN_THREE,        String colOne,        String aceDiamonds,        String ColFour,        String cellFour,        String aceHearts,        String COLUMN_ONE,        String aceClubs,        String DIAMONDS_ACE_PILE,        String cellOne,        String discardPile,        String acespades,        String DECK,        String CELL_TWO,        String DISCARD_PILE,        String SPADES_ACE_PILE,        String ColThree,        String cellThree,        String HEARTS_ACE_PILE,        String CELL_ONE,        String COLUMN_FOUR,        String cellTwo,        String COLUMN_TWO,        String CELL_THREE,        String CLUBS_ACE_PILE,        String CELL_FOUR    ) {
        this.deck = deck;
        this.ColTwo = ColTwo;
        this.COLUMN_THREE = COLUMN_THREE;
        this.colOne = colOne;
        this.aceDiamonds = aceDiamonds;
        this.ColFour = ColFour;
        this.cellFour = cellFour;
        this.aceHearts = aceHearts;
        this.COLUMN_ONE = COLUMN_ONE;
        this.aceClubs = aceClubs;
        this.DIAMONDS_ACE_PILE = DIAMONDS_ACE_PILE;
        this.cellOne = cellOne;
        this.discardPile = discardPile;
        this.acespades = acespades;
        this.DECK = DECK;
        this.CELL_TWO = CELL_TWO;
        this.DISCARD_PILE = DISCARD_PILE;
        this.SPADES_ACE_PILE = SPADES_ACE_PILE;
        this.ColThree = ColThree;
        this.cellThree = cellThree;
        this.HEARTS_ACE_PILE = HEARTS_ACE_PILE;
        this.CELL_ONE = CELL_ONE;
        this.COLUMN_FOUR = COLUMN_FOUR;
        this.cellTwo = cellTwo;
        this.COLUMN_TWO = COLUMN_TWO;
        this.CELL_THREE = CELL_THREE;
        this.CLUBS_ACE_PILE = CLUBS_ACE_PILE;
        this.CELL_FOUR = CELL_FOUR;
    }


    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getColtwo() {
        return ColTwo;
    }

    public void setColtwo(String ColTwo) {
        this.ColTwo = ColTwo;
    }
    public String getColumn_three() {
        return COLUMN_THREE;
    }

    public void setColumn_three(String COLUMN_THREE) {
        this.COLUMN_THREE = COLUMN_THREE;
    }
    public String getColone() {
        return colOne;
    }

    public void setColone(String colOne) {
        this.colOne = colOne;
    }
    public String getAcediamonds() {
        return aceDiamonds;
    }

    public void setAcediamonds(String aceDiamonds) {
        this.aceDiamonds = aceDiamonds;
    }
    public String getColfour() {
        return ColFour;
    }

    public void setColfour(String ColFour) {
        this.ColFour = ColFour;
    }
    public String getCellfour() {
        return cellFour;
    }

    public void setCellfour(String cellFour) {
        this.cellFour = cellFour;
    }
    public String getAcehearts() {
        return aceHearts;
    }

    public void setAcehearts(String aceHearts) {
        this.aceHearts = aceHearts;
    }
    public String getColumn_one() {
        return COLUMN_ONE;
    }

    public void setColumn_one(String COLUMN_ONE) {
        this.COLUMN_ONE = COLUMN_ONE;
    }
    public String getAceclubs() {
        return aceClubs;
    }

    public void setAceclubs(String aceClubs) {
        this.aceClubs = aceClubs;
    }
    public String getDiamonds_ace_pile() {
        return DIAMONDS_ACE_PILE;
    }

    public void setDiamonds_ace_pile(String DIAMONDS_ACE_PILE) {
        this.DIAMONDS_ACE_PILE = DIAMONDS_ACE_PILE;
    }
    public String getCellone() {
        return cellOne;
    }

    public void setCellone(String cellOne) {
        this.cellOne = cellOne;
    }
    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getAcespades() {
        return acespades;
    }

    public void setAcespades(String acespades) {
        this.acespades = acespades;
    }
    public String getDeck() {
        return DECK;
    }

    public void setDeck(String DECK) {
        this.DECK = DECK;
    }
    public String getCell_two() {
        return CELL_TWO;
    }

    public void setCell_two(String CELL_TWO) {
        this.CELL_TWO = CELL_TWO;
    }
    public String getDiscard_pile() {
        return DISCARD_PILE;
    }

    public void setDiscard_pile(String DISCARD_PILE) {
        this.DISCARD_PILE = DISCARD_PILE;
    }
    public String getSpades_ace_pile() {
        return SPADES_ACE_PILE;
    }

    public void setSpades_ace_pile(String SPADES_ACE_PILE) {
        this.SPADES_ACE_PILE = SPADES_ACE_PILE;
    }
    public String getColthree() {
        return ColThree;
    }

    public void setColthree(String ColThree) {
        this.ColThree = ColThree;
    }
    public String getCellthree() {
        return cellThree;
    }

    public void setCellthree(String cellThree) {
        this.cellThree = cellThree;
    }
    public String getHearts_ace_pile() {
        return HEARTS_ACE_PILE;
    }

    public void setHearts_ace_pile(String HEARTS_ACE_PILE) {
        this.HEARTS_ACE_PILE = HEARTS_ACE_PILE;
    }
    public String getCell_one() {
        return CELL_ONE;
    }

    public void setCell_one(String CELL_ONE) {
        this.CELL_ONE = CELL_ONE;
    }
    public String getColumn_four() {
        return COLUMN_FOUR;
    }

    public void setColumn_four(String COLUMN_FOUR) {
        this.COLUMN_FOUR = COLUMN_FOUR;
    }
    public String getCelltwo() {
        return cellTwo;
    }

    public void setCelltwo(String cellTwo) {
        this.cellTwo = cellTwo;
    }
    public String getColumn_two() {
        return COLUMN_TWO;
    }

    public void setColumn_two(String COLUMN_TWO) {
        this.COLUMN_TWO = COLUMN_TWO;
    }
    public String getCell_three() {
        return CELL_THREE;
    }

    public void setCell_three(String CELL_THREE) {
        this.CELL_THREE = CELL_THREE;
    }
    public String getClubs_ace_pile() {
        return CLUBS_ACE_PILE;
    }

    public void setClubs_ace_pile(String CLUBS_ACE_PILE) {
        this.CLUBS_ACE_PILE = CLUBS_ACE_PILE;
    }
    public String getCell_four() {
        return CELL_FOUR;
    }

    public void setCell_four(String CELL_FOUR) {
        this.CELL_FOUR = CELL_FOUR;
    }


}
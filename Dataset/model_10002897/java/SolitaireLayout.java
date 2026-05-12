





import java.util.List;
import java.util.ArrayList;

public class SolitaireLayout  {

    private String DISCARD_PILE;
    private String CELL_TWO;
    private String cellOne;
    private String COLUMEN_ONE;
    private String colTwo;
    private String DECK;
    private String discardPile;
    private String cellThree;
    private String deck;
    private String COLUMN_THREE;
    private String HEARTS_ACE_PILE;
    private String DIAMONDS_ACE_PILE;
    private String COLUMN_FOUR;
    private String aceSpades;
    private String CLUBS_ACE_PILE;
    private String CELL_FOUR;
    private String CELL_ONE;
    private String CELL_THREE;
    private String COLUMN_TWO;
    private String colThree;
    private String cellTwo;
    private String aceClubs;
    private String colOne;
    private String aceDiamonds;
    private String SPADES_ACE_PILE;
    private String cellFour;
    private String aceHearts;
    private String colFour;



    public SolitaireLayout(
        String DISCARD_PILE,        String CELL_TWO,        String cellOne,        String COLUMEN_ONE,        String colTwo,        String DECK,        String discardPile,        String cellThree,        String deck,        String COLUMN_THREE,        String HEARTS_ACE_PILE,        String DIAMONDS_ACE_PILE,        String COLUMN_FOUR,        String aceSpades,        String CLUBS_ACE_PILE,        String CELL_FOUR,        String CELL_ONE,        String CELL_THREE,        String COLUMN_TWO,        String colThree,        String cellTwo,        String aceClubs,        String colOne,        String aceDiamonds,        String SPADES_ACE_PILE,        String cellFour,        String aceHearts,        String colFour    ) {
        this.DISCARD_PILE = DISCARD_PILE;
        this.CELL_TWO = CELL_TWO;
        this.cellOne = cellOne;
        this.COLUMEN_ONE = COLUMEN_ONE;
        this.colTwo = colTwo;
        this.DECK = DECK;
        this.discardPile = discardPile;
        this.cellThree = cellThree;
        this.deck = deck;
        this.COLUMN_THREE = COLUMN_THREE;
        this.HEARTS_ACE_PILE = HEARTS_ACE_PILE;
        this.DIAMONDS_ACE_PILE = DIAMONDS_ACE_PILE;
        this.COLUMN_FOUR = COLUMN_FOUR;
        this.aceSpades = aceSpades;
        this.CLUBS_ACE_PILE = CLUBS_ACE_PILE;
        this.CELL_FOUR = CELL_FOUR;
        this.CELL_ONE = CELL_ONE;
        this.CELL_THREE = CELL_THREE;
        this.COLUMN_TWO = COLUMN_TWO;
        this.colThree = colThree;
        this.cellTwo = cellTwo;
        this.aceClubs = aceClubs;
        this.colOne = colOne;
        this.aceDiamonds = aceDiamonds;
        this.SPADES_ACE_PILE = SPADES_ACE_PILE;
        this.cellFour = cellFour;
        this.aceHearts = aceHearts;
        this.colFour = colFour;
    }


    public String getDiscard_pile() {
        return DISCARD_PILE;
    }

    public void setDiscard_pile(String DISCARD_PILE) {
        this.DISCARD_PILE = DISCARD_PILE;
    }
    public String getCell_two() {
        return CELL_TWO;
    }

    public void setCell_two(String CELL_TWO) {
        this.CELL_TWO = CELL_TWO;
    }
    public String getCellone() {
        return cellOne;
    }

    public void setCellone(String cellOne) {
        this.cellOne = cellOne;
    }
    public String getColumen_one() {
        return COLUMEN_ONE;
    }

    public void setColumen_one(String COLUMEN_ONE) {
        this.COLUMEN_ONE = COLUMEN_ONE;
    }
    public String getColtwo() {
        return colTwo;
    }

    public void setColtwo(String colTwo) {
        this.colTwo = colTwo;
    }
    public String getDeck() {
        return DECK;
    }

    public void setDeck(String DECK) {
        this.DECK = DECK;
    }
    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getCellthree() {
        return cellThree;
    }

    public void setCellthree(String cellThree) {
        this.cellThree = cellThree;
    }
    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getColumn_three() {
        return COLUMN_THREE;
    }

    public void setColumn_three(String COLUMN_THREE) {
        this.COLUMN_THREE = COLUMN_THREE;
    }
    public String getHearts_ace_pile() {
        return HEARTS_ACE_PILE;
    }

    public void setHearts_ace_pile(String HEARTS_ACE_PILE) {
        this.HEARTS_ACE_PILE = HEARTS_ACE_PILE;
    }
    public String getDiamonds_ace_pile() {
        return DIAMONDS_ACE_PILE;
    }

    public void setDiamonds_ace_pile(String DIAMONDS_ACE_PILE) {
        this.DIAMONDS_ACE_PILE = DIAMONDS_ACE_PILE;
    }
    public String getColumn_four() {
        return COLUMN_FOUR;
    }

    public void setColumn_four(String COLUMN_FOUR) {
        this.COLUMN_FOUR = COLUMN_FOUR;
    }
    public String getAcespades() {
        return aceSpades;
    }

    public void setAcespades(String aceSpades) {
        this.aceSpades = aceSpades;
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
    public String getCell_one() {
        return CELL_ONE;
    }

    public void setCell_one(String CELL_ONE) {
        this.CELL_ONE = CELL_ONE;
    }
    public String getCell_three() {
        return CELL_THREE;
    }

    public void setCell_three(String CELL_THREE) {
        this.CELL_THREE = CELL_THREE;
    }
    public String getColumn_two() {
        return COLUMN_TWO;
    }

    public void setColumn_two(String COLUMN_TWO) {
        this.COLUMN_TWO = COLUMN_TWO;
    }
    public String getColthree() {
        return colThree;
    }

    public void setColthree(String colThree) {
        this.colThree = colThree;
    }
    public String getCelltwo() {
        return cellTwo;
    }

    public void setCelltwo(String cellTwo) {
        this.cellTwo = cellTwo;
    }
    public String getAceclubs() {
        return aceClubs;
    }

    public void setAceclubs(String aceClubs) {
        this.aceClubs = aceClubs;
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
    public String getSpades_ace_pile() {
        return SPADES_ACE_PILE;
    }

    public void setSpades_ace_pile(String SPADES_ACE_PILE) {
        this.SPADES_ACE_PILE = SPADES_ACE_PILE;
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
    public String getColfour() {
        return colFour;
    }

    public void setColfour(String colFour) {
        this.colFour = colFour;
    }


}
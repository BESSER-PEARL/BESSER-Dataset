





import java.util.List;
import java.util.ArrayList;

public class SolitaireBoard  {

    private int GAME_WON;
    private int newDifficulty;
    private int timerCount;
    private int GAME_LOST;
    private String timer;
    private int winSoundsStatus;
    private String numCardsInDiscardView;
    private String numCards;
    private String timerLabel;
    private int drawCount;
    private int newDrawCount;
    private int timerToRunNextGame;
    private int backgroundNumber;
    private String statusBar;
    private int RESET_STATS;
    private int winAnimationStatus;
    private boolean timerToRun;
    private int GAME_SAVED;
    private int deckNumber;
    private int DO_NOTHING;
    private int difficulty;





    private List<CardStack> cardstacks;




    private DiscardPile discardpile;




    private Deck deck;




    private List<AcePile> acepiles;




    private List<SingleCell> singlecells;




    private List<Column> columns;


    public SolitaireBoard(
        int GAME_WON,        int newDifficulty,        int timerCount,        int GAME_LOST,        String timer,        int winSoundsStatus,        String numCardsInDiscardView,        String numCards,        String timerLabel,        int drawCount,        int newDrawCount,        int timerToRunNextGame,        int backgroundNumber,        String statusBar,        int RESET_STATS,        int winAnimationStatus,        boolean timerToRun,        int GAME_SAVED,        int deckNumber,        int DO_NOTHING,        int difficulty    ) {
        this.GAME_WON = GAME_WON;
        this.newDifficulty = newDifficulty;
        this.timerCount = timerCount;
        this.GAME_LOST = GAME_LOST;
        this.timer = timer;
        this.winSoundsStatus = winSoundsStatus;
        this.numCardsInDiscardView = numCardsInDiscardView;
        this.numCards = numCards;
        this.timerLabel = timerLabel;
        this.drawCount = drawCount;
        this.newDrawCount = newDrawCount;
        this.timerToRunNextGame = timerToRunNextGame;
        this.backgroundNumber = backgroundNumber;
        this.statusBar = statusBar;
        this.RESET_STATS = RESET_STATS;
        this.winAnimationStatus = winAnimationStatus;
        this.timerToRun = timerToRun;
        this.GAME_SAVED = GAME_SAVED;
        this.deckNumber = deckNumber;
        this.DO_NOTHING = DO_NOTHING;
        this.difficulty = difficulty;
        this.cardstacks = new ArrayList<>();
        this.acepiles = new ArrayList<>();
        this.singlecells = new ArrayList<>();
        this.columns = new ArrayList<>();
    }

    public SolitaireBoard(
        int GAME_WON,        int newDifficulty,        int timerCount,        int GAME_LOST,        String timer,        int winSoundsStatus,        String numCardsInDiscardView,        String numCards,        String timerLabel,        int drawCount,        int newDrawCount,        int timerToRunNextGame,        int backgroundNumber,        String statusBar,        int RESET_STATS,        int winAnimationStatus,        boolean timerToRun,        int GAME_SAVED,        int deckNumber,        int DO_NOTHING,        int difficulty        ArrayList<CardStack> cardstacks,        ArrayList<AcePile> acepiles,        ArrayList<SingleCell> singlecells,        ArrayList<Column> columns    ) {
        this.GAME_WON = GAME_WON;
        this.newDifficulty = newDifficulty;
        this.timerCount = timerCount;
        this.GAME_LOST = GAME_LOST;
        this.timer = timer;
        this.winSoundsStatus = winSoundsStatus;
        this.numCardsInDiscardView = numCardsInDiscardView;
        this.numCards = numCards;
        this.timerLabel = timerLabel;
        this.drawCount = drawCount;
        this.newDrawCount = newDrawCount;
        this.timerToRunNextGame = timerToRunNextGame;
        this.backgroundNumber = backgroundNumber;
        this.statusBar = statusBar;
        this.RESET_STATS = RESET_STATS;
        this.winAnimationStatus = winAnimationStatus;
        this.timerToRun = timerToRun;
        this.GAME_SAVED = GAME_SAVED;
        this.deckNumber = deckNumber;
        this.DO_NOTHING = DO_NOTHING;
        this.difficulty = difficulty;
        this.cardstacks = cardstacks;
        this.acepiles = acepiles;
        this.singlecells = singlecells;
        this.columns = columns;
    }

    public int getGame_won() {
        return GAME_WON;
    }

    public void setGame_won(int GAME_WON) {
        this.GAME_WON = GAME_WON;
    }
    public int getNewdifficulty() {
        return newDifficulty;
    }

    public void setNewdifficulty(int newDifficulty) {
        this.newDifficulty = newDifficulty;
    }
    public int getTimercount() {
        return timerCount;
    }

    public void setTimercount(int timerCount) {
        this.timerCount = timerCount;
    }
    public int getGame_lost() {
        return GAME_LOST;
    }

    public void setGame_lost(int GAME_LOST) {
        this.GAME_LOST = GAME_LOST;
    }
    public String getTimer() {
        return timer;
    }

    public void setTimer(String timer) {
        this.timer = timer;
    }
    public int getWinsoundsstatus() {
        return winSoundsStatus;
    }

    public void setWinsoundsstatus(int winSoundsStatus) {
        this.winSoundsStatus = winSoundsStatus;
    }
    public String getNumcardsindiscardview() {
        return numCardsInDiscardView;
    }

    public void setNumcardsindiscardview(String numCardsInDiscardView) {
        this.numCardsInDiscardView = numCardsInDiscardView;
    }
    public String getNumcards() {
        return numCards;
    }

    public void setNumcards(String numCards) {
        this.numCards = numCards;
    }
    public String getTimerlabel() {
        return timerLabel;
    }

    public void setTimerlabel(String timerLabel) {
        this.timerLabel = timerLabel;
    }
    public int getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(int drawCount) {
        this.drawCount = drawCount;
    }
    public int getNewdrawcount() {
        return newDrawCount;
    }

    public void setNewdrawcount(int newDrawCount) {
        this.newDrawCount = newDrawCount;
    }
    public int getTimertorunnextgame() {
        return timerToRunNextGame;
    }

    public void setTimertorunnextgame(int timerToRunNextGame) {
        this.timerToRunNextGame = timerToRunNextGame;
    }
    public int getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(int backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public String getStatusbar() {
        return statusBar;
    }

    public void setStatusbar(String statusBar) {
        this.statusBar = statusBar;
    }
    public int getReset_stats() {
        return RESET_STATS;
    }

    public void setReset_stats(int RESET_STATS) {
        this.RESET_STATS = RESET_STATS;
    }
    public int getWinanimationstatus() {
        return winAnimationStatus;
    }

    public void setWinanimationstatus(int winAnimationStatus) {
        this.winAnimationStatus = winAnimationStatus;
    }
    public boolean getTimertorun() {
        return timerToRun;
    }

    public void setTimertorun(boolean timerToRun) {
        this.timerToRun = timerToRun;
    }
    public int getGame_saved() {
        return GAME_SAVED;
    }

    public void setGame_saved(int GAME_SAVED) {
        this.GAME_SAVED = GAME_SAVED;
    }
    public int getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(int deckNumber) {
        this.deckNumber = deckNumber;
    }
    public int getDo_nothing() {
        return DO_NOTHING;
    }

    public void setDo_nothing(int DO_NOTHING) {
        this.DO_NOTHING = DO_NOTHING;
    }
    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }

    public List<CardStack> getCardstacks() {
        return cardstacks;
    }

    public void addCardstack(Cardstack cardstack) {
        this.cardstacks.add(cardstack);
    }
    public DiscardPile getDiscardpile() {
        return discardpile;
    }

    public void setDiscardpile(DiscardPile discardpile) {
        this.discardpile = discardpile;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public List<AcePile> getAcepiles() {
        return acepiles;
    }

    public void addAcepile(Acepile acepile) {
        this.acepiles.add(acepile);
    }
    public List<SingleCell> getSinglecells() {
        return singlecells;
    }

    public void addSinglecell(Singlecell singlecell) {
        this.singlecells.add(singlecell);
    }
    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }

}
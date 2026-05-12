





import java.util.List;
import java.util.ArrayList;

public class SolitaireBoard  {

    private int drawCount;
    private int deckNumber;
    private String timerLabel;
    private int RESET_STATS;
    private int newDifficulty;
    private String timer;
    private boolean timerToRun;
    private String statusBar;
    private int GAME_WON;
    private String numCards;
    private int newDrawCount;
    private int GAME_SAVED;
    private int backgroundNumber;
    private int GAME_LOST;
    private int timerToRunNextGame;
    private int timerCount;
    private String numCardsInDiscardView;
    private int winSoundsStatus;
    private int winAnimationStatus;
    private int difficulty;
    private int DO_NOTHING;





    private List<SingleCell> singlecells;




    private Deck deck;




    private List<Column> columns;




    private DiscardPile discardpile;




    private List<CardStack> cardstacks;




    private List<AcePile> acepiles;


    public SolitaireBoard(
        int drawCount,        int deckNumber,        String timerLabel,        int RESET_STATS,        int newDifficulty,        String timer,        boolean timerToRun,        String statusBar,        int GAME_WON,        String numCards,        int newDrawCount,        int GAME_SAVED,        int backgroundNumber,        int GAME_LOST,        int timerToRunNextGame,        int timerCount,        String numCardsInDiscardView,        int winSoundsStatus,        int winAnimationStatus,        int difficulty,        int DO_NOTHING    ) {
        this.drawCount = drawCount;
        this.deckNumber = deckNumber;
        this.timerLabel = timerLabel;
        this.RESET_STATS = RESET_STATS;
        this.newDifficulty = newDifficulty;
        this.timer = timer;
        this.timerToRun = timerToRun;
        this.statusBar = statusBar;
        this.GAME_WON = GAME_WON;
        this.numCards = numCards;
        this.newDrawCount = newDrawCount;
        this.GAME_SAVED = GAME_SAVED;
        this.backgroundNumber = backgroundNumber;
        this.GAME_LOST = GAME_LOST;
        this.timerToRunNextGame = timerToRunNextGame;
        this.timerCount = timerCount;
        this.numCardsInDiscardView = numCardsInDiscardView;
        this.winSoundsStatus = winSoundsStatus;
        this.winAnimationStatus = winAnimationStatus;
        this.difficulty = difficulty;
        this.DO_NOTHING = DO_NOTHING;
        this.singlecells = new ArrayList<>();
        this.columns = new ArrayList<>();
        this.cardstacks = new ArrayList<>();
        this.acepiles = new ArrayList<>();
    }

    public SolitaireBoard(
        int drawCount,        int deckNumber,        String timerLabel,        int RESET_STATS,        int newDifficulty,        String timer,        boolean timerToRun,        String statusBar,        int GAME_WON,        String numCards,        int newDrawCount,        int GAME_SAVED,        int backgroundNumber,        int GAME_LOST,        int timerToRunNextGame,        int timerCount,        String numCardsInDiscardView,        int winSoundsStatus,        int winAnimationStatus,        int difficulty,        int DO_NOTHING        ArrayList<SingleCell> singlecells,        ArrayList<Column> columns,        ArrayList<CardStack> cardstacks,        ArrayList<AcePile> acepiles    ) {
        this.drawCount = drawCount;
        this.deckNumber = deckNumber;
        this.timerLabel = timerLabel;
        this.RESET_STATS = RESET_STATS;
        this.newDifficulty = newDifficulty;
        this.timer = timer;
        this.timerToRun = timerToRun;
        this.statusBar = statusBar;
        this.GAME_WON = GAME_WON;
        this.numCards = numCards;
        this.newDrawCount = newDrawCount;
        this.GAME_SAVED = GAME_SAVED;
        this.backgroundNumber = backgroundNumber;
        this.GAME_LOST = GAME_LOST;
        this.timerToRunNextGame = timerToRunNextGame;
        this.timerCount = timerCount;
        this.numCardsInDiscardView = numCardsInDiscardView;
        this.winSoundsStatus = winSoundsStatus;
        this.winAnimationStatus = winAnimationStatus;
        this.difficulty = difficulty;
        this.DO_NOTHING = DO_NOTHING;
        this.singlecells = singlecells;
        this.columns = columns;
        this.cardstacks = cardstacks;
        this.acepiles = acepiles;
    }

    public int getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(int drawCount) {
        this.drawCount = drawCount;
    }
    public int getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(int deckNumber) {
        this.deckNumber = deckNumber;
    }
    public String getTimerlabel() {
        return timerLabel;
    }

    public void setTimerlabel(String timerLabel) {
        this.timerLabel = timerLabel;
    }
    public int getReset_stats() {
        return RESET_STATS;
    }

    public void setReset_stats(int RESET_STATS) {
        this.RESET_STATS = RESET_STATS;
    }
    public int getNewdifficulty() {
        return newDifficulty;
    }

    public void setNewdifficulty(int newDifficulty) {
        this.newDifficulty = newDifficulty;
    }
    public String getTimer() {
        return timer;
    }

    public void setTimer(String timer) {
        this.timer = timer;
    }
    public boolean getTimertorun() {
        return timerToRun;
    }

    public void setTimertorun(boolean timerToRun) {
        this.timerToRun = timerToRun;
    }
    public String getStatusbar() {
        return statusBar;
    }

    public void setStatusbar(String statusBar) {
        this.statusBar = statusBar;
    }
    public int getGame_won() {
        return GAME_WON;
    }

    public void setGame_won(int GAME_WON) {
        this.GAME_WON = GAME_WON;
    }
    public String getNumcards() {
        return numCards;
    }

    public void setNumcards(String numCards) {
        this.numCards = numCards;
    }
    public int getNewdrawcount() {
        return newDrawCount;
    }

    public void setNewdrawcount(int newDrawCount) {
        this.newDrawCount = newDrawCount;
    }
    public int getGame_saved() {
        return GAME_SAVED;
    }

    public void setGame_saved(int GAME_SAVED) {
        this.GAME_SAVED = GAME_SAVED;
    }
    public int getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(int backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public int getGame_lost() {
        return GAME_LOST;
    }

    public void setGame_lost(int GAME_LOST) {
        this.GAME_LOST = GAME_LOST;
    }
    public int getTimertorunnextgame() {
        return timerToRunNextGame;
    }

    public void setTimertorunnextgame(int timerToRunNextGame) {
        this.timerToRunNextGame = timerToRunNextGame;
    }
    public int getTimercount() {
        return timerCount;
    }

    public void setTimercount(int timerCount) {
        this.timerCount = timerCount;
    }
    public String getNumcardsindiscardview() {
        return numCardsInDiscardView;
    }

    public void setNumcardsindiscardview(String numCardsInDiscardView) {
        this.numCardsInDiscardView = numCardsInDiscardView;
    }
    public int getWinsoundsstatus() {
        return winSoundsStatus;
    }

    public void setWinsoundsstatus(int winSoundsStatus) {
        this.winSoundsStatus = winSoundsStatus;
    }
    public int getWinanimationstatus() {
        return winAnimationStatus;
    }

    public void setWinanimationstatus(int winAnimationStatus) {
        this.winAnimationStatus = winAnimationStatus;
    }
    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }
    public int getDo_nothing() {
        return DO_NOTHING;
    }

    public void setDo_nothing(int DO_NOTHING) {
        this.DO_NOTHING = DO_NOTHING;
    }

    public List<SingleCell> getSinglecells() {
        return singlecells;
    }

    public void addSinglecell(Singlecell singlecell) {
        this.singlecells.add(singlecell);
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }
    public DiscardPile getDiscardpile() {
        return discardpile;
    }

    public void setDiscardpile(DiscardPile discardpile) {
        this.discardpile = discardpile;
    }
    public List<CardStack> getCardstacks() {
        return cardstacks;
    }

    public void addCardstack(Cardstack cardstack) {
        this.cardstacks.add(cardstack);
    }
    public List<AcePile> getAcepiles() {
        return acepiles;
    }

    public void addAcepile(Acepile acepile) {
        this.acepiles.add(acepile);
    }

}
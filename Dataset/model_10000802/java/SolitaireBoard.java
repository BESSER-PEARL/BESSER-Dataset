





import java.util.List;
import java.util.ArrayList;

public class SolitaireBoard  {

    private String numCardsInDiscardView;
    private String backgroundNumber;
    private boolean timerToRun;
    private String timerToRunNextGame;
    private String drawCount;
    private String numCards;
    private String discardPile;
    private String deckNumber;
    private None deck;
    private String wl;
    private String ml;
    private String statusBar;
    private String DO_NOTHING;
    private String GAME_SAVED;
    private String columns;
    private String newDifficulty;
    private String RESET_STATS;
    private String winAnimationStatus;
    private None dealDeck;
    private String GAME_WON;
    private String timer;
    private String newDrawCount;
    private String destinationList;
    private String GAME_LOST;
    private String mainPanel;
    private String sourceList;
    private String cells;
    private String timerLabel;
    private String acePiles;
    private String timerCount;



    public SolitaireBoard(
        String numCardsInDiscardView,        String backgroundNumber,        boolean timerToRun,        String timerToRunNextGame,        String drawCount,        String numCards,        String discardPile,        String deckNumber,        None deck,        String wl,        String ml,        String statusBar,        String DO_NOTHING,        String GAME_SAVED,        String columns,        String newDifficulty,        String RESET_STATS,        String winAnimationStatus,        None dealDeck,        String GAME_WON,        String timer,        String newDrawCount,        String destinationList,        String GAME_LOST,        String mainPanel,        String sourceList,        String cells,        String timerLabel,        String acePiles,        String timerCount    ) {
        this.numCardsInDiscardView = numCardsInDiscardView;
        this.backgroundNumber = backgroundNumber;
        this.timerToRun = timerToRun;
        this.timerToRunNextGame = timerToRunNextGame;
        this.drawCount = drawCount;
        this.numCards = numCards;
        this.discardPile = discardPile;
        this.deckNumber = deckNumber;
        this.deck = deck;
        this.wl = wl;
        this.ml = ml;
        this.statusBar = statusBar;
        this.DO_NOTHING = DO_NOTHING;
        this.GAME_SAVED = GAME_SAVED;
        this.columns = columns;
        this.newDifficulty = newDifficulty;
        this.RESET_STATS = RESET_STATS;
        this.winAnimationStatus = winAnimationStatus;
        this.dealDeck = dealDeck;
        this.GAME_WON = GAME_WON;
        this.timer = timer;
        this.newDrawCount = newDrawCount;
        this.destinationList = destinationList;
        this.GAME_LOST = GAME_LOST;
        this.mainPanel = mainPanel;
        this.sourceList = sourceList;
        this.cells = cells;
        this.timerLabel = timerLabel;
        this.acePiles = acePiles;
        this.timerCount = timerCount;
    }


    public String getNumcardsindiscardview() {
        return numCardsInDiscardView;
    }

    public void setNumcardsindiscardview(String numCardsInDiscardView) {
        this.numCardsInDiscardView = numCardsInDiscardView;
    }
    public String getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(String backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public boolean getTimertorun() {
        return timerToRun;
    }

    public void setTimertorun(boolean timerToRun) {
        this.timerToRun = timerToRun;
    }
    public String getTimertorunnextgame() {
        return timerToRunNextGame;
    }

    public void setTimertorunnextgame(String timerToRunNextGame) {
        this.timerToRunNextGame = timerToRunNextGame;
    }
    public String getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(String drawCount) {
        this.drawCount = drawCount;
    }
    public String getNumcards() {
        return numCards;
    }

    public void setNumcards(String numCards) {
        this.numCards = numCards;
    }
    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(String deckNumber) {
        this.deckNumber = deckNumber;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public String getWl() {
        return wl;
    }

    public void setWl(String wl) {
        this.wl = wl;
    }
    public String getMl() {
        return ml;
    }

    public void setMl(String ml) {
        this.ml = ml;
    }
    public String getStatusbar() {
        return statusBar;
    }

    public void setStatusbar(String statusBar) {
        this.statusBar = statusBar;
    }
    public String getDo_nothing() {
        return DO_NOTHING;
    }

    public void setDo_nothing(String DO_NOTHING) {
        this.DO_NOTHING = DO_NOTHING;
    }
    public String getGame_saved() {
        return GAME_SAVED;
    }

    public void setGame_saved(String GAME_SAVED) {
        this.GAME_SAVED = GAME_SAVED;
    }
    public String getColumns() {
        return columns;
    }

    public void setColumns(String columns) {
        this.columns = columns;
    }
    public String getNewdifficulty() {
        return newDifficulty;
    }

    public void setNewdifficulty(String newDifficulty) {
        this.newDifficulty = newDifficulty;
    }
    public String getReset_stats() {
        return RESET_STATS;
    }

    public void setReset_stats(String RESET_STATS) {
        this.RESET_STATS = RESET_STATS;
    }
    public String getWinanimationstatus() {
        return winAnimationStatus;
    }

    public void setWinanimationstatus(String winAnimationStatus) {
        this.winAnimationStatus = winAnimationStatus;
    }
    public None getDealdeck() {
        return dealDeck;
    }

    public void setDealdeck(None dealDeck) {
        this.dealDeck = dealDeck;
    }
    public String getGame_won() {
        return GAME_WON;
    }

    public void setGame_won(String GAME_WON) {
        this.GAME_WON = GAME_WON;
    }
    public String getTimer() {
        return timer;
    }

    public void setTimer(String timer) {
        this.timer = timer;
    }
    public String getNewdrawcount() {
        return newDrawCount;
    }

    public void setNewdrawcount(String newDrawCount) {
        this.newDrawCount = newDrawCount;
    }
    public String getDestinationlist() {
        return destinationList;
    }

    public void setDestinationlist(String destinationList) {
        this.destinationList = destinationList;
    }
    public String getGame_lost() {
        return GAME_LOST;
    }

    public void setGame_lost(String GAME_LOST) {
        this.GAME_LOST = GAME_LOST;
    }
    public String getMainpanel() {
        return mainPanel;
    }

    public void setMainpanel(String mainPanel) {
        this.mainPanel = mainPanel;
    }
    public String getSourcelist() {
        return sourceList;
    }

    public void setSourcelist(String sourceList) {
        this.sourceList = sourceList;
    }
    public String getCells() {
        return cells;
    }

    public void setCells(String cells) {
        this.cells = cells;
    }
    public String getTimerlabel() {
        return timerLabel;
    }

    public void setTimerlabel(String timerLabel) {
        this.timerLabel = timerLabel;
    }
    public String getAcepiles() {
        return acePiles;
    }

    public void setAcepiles(String acePiles) {
        this.acePiles = acePiles;
    }
    public String getTimercount() {
        return timerCount;
    }

    public void setTimercount(String timerCount) {
        this.timerCount = timerCount;
    }


}
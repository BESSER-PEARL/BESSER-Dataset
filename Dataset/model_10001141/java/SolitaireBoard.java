





import java.util.List;
import java.util.ArrayList;

public class SolitaireBoard  {

    private String GAME_SAVED;
    private boolean timerToRun;
    private String acePiles;
    private String timerCount;
    private String winAnimationStatus;
    private None dealDeck;
    private String cells;
    private String backgroundNumber;
    private String newDrawCount;
    private String RESET_STATS;
    private String timerToRunNextGame;
    private String GAME_WON;
    private String timerLabel;
    private String DO_NOTHING;
    private String statusBar;
    private String discardPile;
    private String columns;
    private String ml;
    private String newDifficulty;
    private String mainPanel;
    private String wl;
    private String deckNumber;
    private None deck;
    private String sourceList;
    private String numCards;
    private String drawCount;
    private String GAME_LOST;
    private String numCardsInDiscardView;
    private String destinationList;
    private String timer;



    public SolitaireBoard(
        String GAME_SAVED,        boolean timerToRun,        String acePiles,        String timerCount,        String winAnimationStatus,        None dealDeck,        String cells,        String backgroundNumber,        String newDrawCount,        String RESET_STATS,        String timerToRunNextGame,        String GAME_WON,        String timerLabel,        String DO_NOTHING,        String statusBar,        String discardPile,        String columns,        String ml,        String newDifficulty,        String mainPanel,        String wl,        String deckNumber,        None deck,        String sourceList,        String numCards,        String drawCount,        String GAME_LOST,        String numCardsInDiscardView,        String destinationList,        String timer    ) {
        this.GAME_SAVED = GAME_SAVED;
        this.timerToRun = timerToRun;
        this.acePiles = acePiles;
        this.timerCount = timerCount;
        this.winAnimationStatus = winAnimationStatus;
        this.dealDeck = dealDeck;
        this.cells = cells;
        this.backgroundNumber = backgroundNumber;
        this.newDrawCount = newDrawCount;
        this.RESET_STATS = RESET_STATS;
        this.timerToRunNextGame = timerToRunNextGame;
        this.GAME_WON = GAME_WON;
        this.timerLabel = timerLabel;
        this.DO_NOTHING = DO_NOTHING;
        this.statusBar = statusBar;
        this.discardPile = discardPile;
        this.columns = columns;
        this.ml = ml;
        this.newDifficulty = newDifficulty;
        this.mainPanel = mainPanel;
        this.wl = wl;
        this.deckNumber = deckNumber;
        this.deck = deck;
        this.sourceList = sourceList;
        this.numCards = numCards;
        this.drawCount = drawCount;
        this.GAME_LOST = GAME_LOST;
        this.numCardsInDiscardView = numCardsInDiscardView;
        this.destinationList = destinationList;
        this.timer = timer;
    }


    public String getGame_saved() {
        return GAME_SAVED;
    }

    public void setGame_saved(String GAME_SAVED) {
        this.GAME_SAVED = GAME_SAVED;
    }
    public boolean getTimertorun() {
        return timerToRun;
    }

    public void setTimertorun(boolean timerToRun) {
        this.timerToRun = timerToRun;
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
    public String getCells() {
        return cells;
    }

    public void setCells(String cells) {
        this.cells = cells;
    }
    public String getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(String backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public String getNewdrawcount() {
        return newDrawCount;
    }

    public void setNewdrawcount(String newDrawCount) {
        this.newDrawCount = newDrawCount;
    }
    public String getReset_stats() {
        return RESET_STATS;
    }

    public void setReset_stats(String RESET_STATS) {
        this.RESET_STATS = RESET_STATS;
    }
    public String getTimertorunnextgame() {
        return timerToRunNextGame;
    }

    public void setTimertorunnextgame(String timerToRunNextGame) {
        this.timerToRunNextGame = timerToRunNextGame;
    }
    public String getGame_won() {
        return GAME_WON;
    }

    public void setGame_won(String GAME_WON) {
        this.GAME_WON = GAME_WON;
    }
    public String getTimerlabel() {
        return timerLabel;
    }

    public void setTimerlabel(String timerLabel) {
        this.timerLabel = timerLabel;
    }
    public String getDo_nothing() {
        return DO_NOTHING;
    }

    public void setDo_nothing(String DO_NOTHING) {
        this.DO_NOTHING = DO_NOTHING;
    }
    public String getStatusbar() {
        return statusBar;
    }

    public void setStatusbar(String statusBar) {
        this.statusBar = statusBar;
    }
    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getColumns() {
        return columns;
    }

    public void setColumns(String columns) {
        this.columns = columns;
    }
    public String getMl() {
        return ml;
    }

    public void setMl(String ml) {
        this.ml = ml;
    }
    public String getNewdifficulty() {
        return newDifficulty;
    }

    public void setNewdifficulty(String newDifficulty) {
        this.newDifficulty = newDifficulty;
    }
    public String getMainpanel() {
        return mainPanel;
    }

    public void setMainpanel(String mainPanel) {
        this.mainPanel = mainPanel;
    }
    public String getWl() {
        return wl;
    }

    public void setWl(String wl) {
        this.wl = wl;
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
    public String getSourcelist() {
        return sourceList;
    }

    public void setSourcelist(String sourceList) {
        this.sourceList = sourceList;
    }
    public String getNumcards() {
        return numCards;
    }

    public void setNumcards(String numCards) {
        this.numCards = numCards;
    }
    public String getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(String drawCount) {
        this.drawCount = drawCount;
    }
    public String getGame_lost() {
        return GAME_LOST;
    }

    public void setGame_lost(String GAME_LOST) {
        this.GAME_LOST = GAME_LOST;
    }
    public String getNumcardsindiscardview() {
        return numCardsInDiscardView;
    }

    public void setNumcardsindiscardview(String numCardsInDiscardView) {
        this.numCardsInDiscardView = numCardsInDiscardView;
    }
    public String getDestinationlist() {
        return destinationList;
    }

    public void setDestinationlist(String destinationList) {
        this.destinationList = destinationList;
    }
    public String getTimer() {
        return timer;
    }

    public void setTimer(String timer) {
        this.timer = timer;
    }


}